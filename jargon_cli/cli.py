import os
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
            print(file.read())        

    def execute(self, proc):
        self.cli(start_input=f'/execute {proc}')
    
    def __procpath(self, proc):
        if not proc.endswith('.jarg'):
            proc += '.jarg'
        procpath = os.path.join(self.jargdir, proc)
        if not os.path.exists(procpath):
            raise Exception(f'Unknown procedure: {procpath}')
        return procpath
        
    def __execute(self, proc):
        procpath = self.__procpath(proc)
        with open(procpath, 'r') as file:
            proctxt = file.read()
            print(proctxt, end='')
            result = self.conversation.predict(input=f"Execute the following Jargon procedure and print only its output:\n{proctxt}")
            print(result)

    def cli(self, start_input=None):
        procs = [file for file in self.__ls()]
        autocomp = ['/exit', '/ls', '/cat', '/edit', '/execute'] + procs
        jargon_completer = WordCompleter(autocomp, ignore_case=True)

        while True:
            user_input = ""
            if start_input:
                user_input = start_input
                start_input = None
            else:
                user_input = Prompt('> ', 
                    history=FileHistory('history.txt'),
                    auto_suggest=AutoSuggestFromHistory(),
                    completer=jargon_completer,
                ).strip()
        
            if user_input == '/exit':
                return
            
            if user_input == '/ls':
               self.ls()
               continue

            if user_input.startswith('/cat'):
                proc = user_input.split(' ')
                if len(proc) < 2:
                    print('you must specify a procedure')
                else:
                    self.cat(proc[1])
                continue
            
            if user_input.startswith('/execute'):
                proc = user_input.split(' ')
                if len(proc) < 2:
                    print('you must specify a procedure')
                else:
                    proc = proc[1]
                    self.__execute(proc)
                continue

            if user_input.startswith('/'):
                print('input:', user_input[1:])
                self.__execute(user_input[1:])
                continue

            if user_input.startswith('/edit'):
                proc = user_input.split(' ')
                if len(proc) < 2:
                    print('you must specify a procedure')
                else:
                    procpath = self.__procpath(proc[1])
                    click.edit(filename=procpath)
                continue
                        
            result = self.conversation.predict(input=user_input)
            print(result)