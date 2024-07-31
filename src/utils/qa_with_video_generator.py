from src.common.config import Config
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_cohere.embeddings import CohereEmbeddings
from src.prompts.structured_prompts import QA_PROMPT

class QAGenerator:
    def __init__(self, qa_text,query):
        self.qa_text= qa_text
        self.seq_length= 3000
        self.query= query
        self._llm= Config().get_llm()
        self._chain= Config.create_llm_chain(self._llm, QA_PROMPT)


    def text_splitter(self):
        text_splitter=CharacterTextSplitter
        qa_split_text= text_splitter.split_text(self.qa_text)
        return qa_split_text
    
    def qa_generator(self):
        embeddings= CohereEmbeddings()
        textsearch= FAISS.from_texts(self._text_splitter(),embeddings)
        similarity_texts_lists= textsearch.similarity_search(self.query,k=4)
        similarity_texts= ""

        for text in similarity_texts_lists:
            similarity_texts+= f"{text.page_content}"
        
        result= self._chain.run(text=similarity_texts,query= self.query)
        return result