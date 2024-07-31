import os
import re
import pandas as pd
from src.common.config import Config
from pandas import DataFrame
from src.prompts.structured_prompts import PLOT_PROMPT
from pandasai import PandasAI
from src.exceptions.plot_exception import PlotException
import logging

logging.basicConfig(filename='newfile.log',format='%(asctime)s %(message)s', filemode='w')
logger= logging.getLogger()
logger.setLevel(logging.INFO)

class ScoreAnalyzer:
    """
    
    """

    def __init__(self, file_path) -> None:
        if not os.path.exists(file_path):
            raise Exception("")
        self.file_path = file_path
        self.df= pd.read_csv(file_path)
        self._schema_str= self._get_df_schema(self.df)
        self._llm= Config().get_llm()
        self._plot_chain= Config().create_llm_chain(self._llm,PLOT_PROMPT)

    def plot_df(self,desc:str):
        instruction= f"The purpose of the plot: {desc}"
        logger.info(f"{instruction}")
        response= self._plot_chain.run(
            columns=self._schema_str,
            example= self.df.head(1).to_string(),
            file_path= self.file_path,
            instruction= instruction)
        
        codeblocks= self._get_code_blocks(response)
        result={
            "codeblocks":codeblocks,
            "response":response
        }
        print(f"code:{ result['codeblocks']} resp:{ result['response']}")
        return result
    
    def chat_with_data(self,desc)->str:
        """
        """
        desc+="Please provide a Clear and Consise reply"
        pandas_ai=PandasAI(self._llm, conversational= False)
        response= pandas_ai.run(self.df, desc)
        return response
    
    @staticmethod
    def _get_df_schema(df:DataFrame):
        return "\n" .join([f"{name}: {dtype}" for name,dtype in df.dtypes.items()])

    @staticmethod 
    def _get_code_blocks(markdown:str)->str:
        pattern=r"```python(.*?)```"
        code_blocks= re.findall(pattern,markdown, re.DOTALL)
        if len(code_blocks)== 0:
            raise PlotException("No code blocks found")
        else:
             return "\n" .join(code_blocks)