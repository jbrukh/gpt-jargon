import os
import re
import pkg_resources
import click

from langchain.prompts import (
    ChatPromptTemplate, 
    MessagesPlaceholder, 
    SystemMessagePromptTemplate, 
    HumanMessagePromptTemplate,
    PromptTemplate
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

from prompt_toolkit import prompt as Prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion.word_completer import WordCompleter


class JargonCli:

    def __init__(self, jargon_dir=os.path.expanduser('~/.jargon'), model_name='gpt-4'):
        self.jargdir = jargon_dir
        self.__ensure_jargdir()
        self.llm = ChatOpenAI(temperature=0, model_name=model_name)
        self.memory = ConversationBufferMemory(return_messages=True)
        self.jargon_spec = pkg_resources.resource_string(__name__, '../jargon.md').decode('utf-8').replace('{', '{{').replace('}', '}}')
        self.prompt = ChatPromptTemplate.from_messages([
            SystemMessage(content=self.jargon_spec),
            MessagesPlaceholder(variable_name="history"),
            HumanMessagePromptTemplate(prompt=PromptTemplate(template="{input}", input_variables=['input']))
        ])
        self.conversation = ConversationChain(memory=self.memory, prompt=self.prompt, llm=self.llm)


   
    def __ensure_jargdir(self):
        '''Creates `self.jargdir` if it doesn't already exist.'''
        if not os.path.exists(self.jargdir):
            os.makedirs(self.jargdir)
    
    def __ls(self):
        '''Yields all the .jarg files inside of the Jargon directory.'''
        for file in os.listdir(self.jargdir):
            if file.endswith(".jarg"):
                yield file
  
    def ls(self):
        '''Prints all the .jarg files inside of the Jargon directory.'''
        for file in self.__ls():
            print('*', file)

    def cat(self, proc):
        if not proc.endswith('.jarg'):
            proc += '.jarg'
        procpath = os.path.join(self.jargdir, proc)
        with open(procpath, 'r') as file:
            print(file.read(), end='')        

    def execute(self, proc):
        self.cli(start_input=f'/execute {proc}')
    
    def __procpath(self, proc, check_exists=True):
        if not proc.endswith('.jarg'):
            proc += '.jarg'
        procpath = os.path.join(self.jargdir, proc)
        if check_exists and not os.path.exists(procpath):
            raise Exception(f'Unknown procedure: {procpath}')
        return procpath
        
    def __execute(self, proc):
        procpath = self.__procpath(proc)
        with open(procpath, 'r') as file:
            proctxt = file.read()
            print(proctxt, end='')
            result = self.conversation.predict(input=f"Execute the following Jargon procedure and print only its output. If there is no output, print nothing:\n{proctxt}")
            print(result)

    def cli(self, start_input=None):
        procs = [file for file in self.__ls()]
        autocomp = ['/exit', '/ls', '/cat', '/edit', '/execute'] + procs
        jargon_completer = WordCompleter(autocomp, ignore_case=True)
        pattern = re.compile(r'^/([a-zA-Z][a-zA-Z0-9]*(?:-[a-zA-Z0-9]+)*)(?:\s+(\S+))?')
        user_input = start_input

        while True:
            if not user_input:
                user_input = Prompt('> ', 
                    history=FileHistory('history.txt'),
                    auto_suggest=AutoSuggestFromHistory(),
                    completer=jargon_completer,
                ).strip()

            m = pattern.match(user_input)
            raw_input, user_input = user_input, None
                
            if m:
                cmd, arg = m.group(1), m.group(2)
                if cmd == 'exit':
                    return
                        
                if cmd == 'ls':
                    self.ls()
                    continue
                
                if not arg and cmd in ['cat', 'execute', 'edit']:
                    print('you must specify an argument')
                    continue

                if cmd == 'cat':
                    self.cat(arg)
                    continue
                
                if cmd == 'execute':
                    self.__execute(arg)
                    continue
                
                if cmd == 'edit':
                    click.edit(filename=self.__procpath(arg, check_exists=False))
                    continue

                if cmd:
                    try:
                        cmd = self.__procpath(cmd)
                    except:
                        print(f'unknown command or procedure: {cmd}')
                        continue
                    self.__execute(cmd)
                    continue
                        
            result = self.conversation.predict(input=raw_input)
            print(result)
