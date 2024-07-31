from langchain.prompts import PromptTemplate
from src.prompts.analyzer_prompt import PLOT_PROMPT_TEMPLATE
from src.prompts.question_prompt import VERIFY_ANSWER_TEMPLATE,QUESTION_CHOICE_TEMPLATE,QUESTION_SHORT_ANSWER_TEMPLATE 
from src.prompts.summary_prompt import SUMMARY_TEMPLATE, DESCRIPTION_TEMPLATE, QA_TEMPLATE


PLOT_PROMPT= PromptTemplate(input_variables=["columns","example","file_path","instruction"], template=PLOT_PROMPT_TEMPLATE)

SUMMARY_PROMPT= PromptTemplate(input_variables=['summary_count', 'subtitle'], template=SUMMARY_TEMPLATE)

DESCRIPTION_PROMPT= PromptTemplate(input_variables=['description_num',"text"], template= DESCRIPTION_TEMPLATE)

QUESTION_CHOICE_PROMPT= PromptTemplate(input_variables=['instruction',"subject"], template= QUESTION_CHOICE_TEMPLATE)

QUESTION_SHORT_ANSWER_PROMPT= PromptTemplate(input_variables=['instruction',"subject"], template= QUESTION_SHORT_ANSWER_TEMPLATE)

VERIFY_ANSWER_PROMPT=PromptTemplate(input_variables=['question',"answer"], template= VERIFY_ANSWER_TEMPLATE)

QA_PROMPT= PromptTemplate(input_variables=["text","query"],template=QA_TEMPLATE)