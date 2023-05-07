import os
import pkg_resources

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

class JargonCli:

    def __init__(self, jargon_dir=os.path.expanduser('~/.jargon'), model_name='gpt-4'):
        self.jargdir = jargon_dir
        self.__ensure_jargdir()
        self.llm = ChatOpenAI(temperature=0, model_name=model_name)
        self.memory = ConversationBufferMemory(return_messages=True)
        self.jargon_prompt = pkg_resources.resource_string(__name__, '../jargon.md').decode('utf-8')

   
    def __ensure_jargdir(self):
        '''Creates `self.jargdir` if it doesn't already exist.'''
        if not os.path.exists(self.jargdir):
            os.makedirs(self.jargdir)
    
    def ls(self):
        '''Yields all the .jarg files inside of the Jargon directory.'''
        for file in os.listdir(self.jargdir):
            if file.endswith(".jarg"):
                yield file
  
    def execute(self, proc):
        if not proc.endswith('.jarg'):
            proc += '.jarg'
        procpath = os.path.join(self.jargdir, proc)
        if not os.path.exists(procpath):
            raise Exception(f'Unknown procedure: {procpath}')
        

        # prompt template
        prompt = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate(prompt=PromptTemplate(template=self.jargon_prompt.replace('{', '{{').replace('}', '}}'), input_variables=[])),
            MessagesPlaceholder(variable_name="history"),
            HumanMessagePromptTemplate(prompt=PromptTemplate(template="{input}", input_variables=['input']))
        ])
        print(prompt)

        conversation = ConversationChain(memory=self.memory, prompt=prompt, llm=self.llm)

        with open(procpath, 'r') as file:
            proctxt = file.read()
            print(proctxt)
            result = conversation.predict(input=f"Execute the following Jargon procedure and print only its output:\n{proctxt}")
            print(result)

        while True:
            txt = input('\n> ')
            result = conversation.predict(input=txt)
            print(result)
    
    def cli(self):
        return None
