from src.common.config import Config
from src.prompts.structured_prompts import (QUESTION_CHOICE_PROMPT,VERIFY_ANSWER_PROMPT,QUESTION_SHORT_ANSWER_PROMPT )
from src.utils.cache_handler import CacheHandler
from src.entity.subject import SubjectType
from src.entity.question_result import ChoiceQuestionResult, ShortAnswerQuestionResult

class QuestionAssistant:
    def __init__(self) -> None:
        self._llm= Config().get_llm()
        self._set_choice_question_chain= Config.create_llm_chain(llm= self._llm,prompt= QUESTION_CHOICE_PROMPT)
        self._set_short_answer_question_chain= Config.create_llm_chain(llm= self._llm)

        self._verify_answer_chain= Config.create_llm_chain(llm= self._llm, prompt=VERIFY_ANSWER_PROMPT)
        self._cache_handler= CacheHandler()


    def generate_choice_question(self, desc:str, subject_type:str):
        response= self._set_choice_question_chain.run(instruction=desc, subject=SubjectType.get(subject_type))
        choice_question_result= ChoiceQuestionResult(response)
        self._cache_handler.question_cache(subject_type,choice_question_result)
        return choice_question_result
    
    def generate_short_answer_question(self, desc, subject_type):
        response = self._set_short_answer_question_chain.run(instruction=desc, subject=SubjectType.get(subject_type))
        short_answer_result= ShortAnswerQuestionResult(response)
        self._cache_handler.question_cache(subject_type,short_answer_result)
        return short_answer_result
    

    def generate_choice_question_from_context(self,context,desc,subject_type):
        response= self._set_choice_question_chain.run(summary=context,instruction=desc, subject=SubjectType.get(subject_type))
        choice_question_result= ChoiceQuestionResult(response)
        self._cache_handler.question_cache(subject_type,choice_question_result)
        return choice_question_result
    
    def generate_short_answer_question_from_context(self,context,desc,subject_type):
        response= self._set_short_answer_question_chain.run(summary=context,instruction=desc, subject=SubjectType.get(subject_type))
        short_answer_result= ShortAnswerQuestionResult(response)
        self._cache_handler.question_cache(subject_type,short_answer_result)
        return short_answer_result
    
    def verify_question(self,question,answer):
        self._verify_answer_chain.run(question= question, answer= answer)