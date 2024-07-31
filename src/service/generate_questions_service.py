import gradio as gr
from utils.question_assistant import QuestionAssistant
from utils.cache_handler import CacheHandler
from entity.question_result import ChoiceQuestionResult, ShortAnswerQuestionResult
from src.utils.question_assistant import QuestionAssistant

def generate_question(question_type, desc, subject):
    question_assistant= QuestionAssistant()
    question=""

    if question_type=="MCQ":
        result = question_assistant.generate_choice_question(desc, subject)
        question= ChoiceQuestionResult.get_choice_question(result)["question"]
    if question_type=="Short":
        result=question_assistant.generate_short_answer_question(desc,subject)
        question= ShortAnswerQuestionResult.get_short_answer_question(result)["question"]

    return gr.update(value= question)

def remove_question(question, subject_type):
    if ChoiceQuestionResult:
        cache_handler= CacheHandler()
        cache_handler.pop_question(subject_type)
        return gr.update(value="")
    
    else:
        raise gr.Error("")
