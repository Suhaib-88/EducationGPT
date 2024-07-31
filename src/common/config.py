import os
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.llm import LLMChain
from langchain.prompts import BaseChatPromptTemplate

class Config:        
    def get_llm(self):
        llm= self._get_model()
        return llm
    
    @staticmethod
    def create_llm_chain(llm,prompt:BaseChatPromptTemplate)-> LLMChain:
        return LLMChain(llm= llm, prompt= prompt)
   
    @staticmethod
    def _get_model():
        model= os.getenv("MODEL")
        if model is None:
            raise ValueError("Model not set in")
        
        if model == "gemini":
            return ChatGoogleGenerativeAI(model="gemini-pro")

        elif model == "groq":
            return ChatGroq(temperature=0.6, model_name="llama-3.1-70b-versatile")