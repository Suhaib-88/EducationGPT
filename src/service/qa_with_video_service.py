from src.utils.qa_with_video_generator import QAGenerator

def generate_qa(qa_text,query,chat_history):
    bot_message= QAGenerator(qa_text,query).qa_generator()
    chat_history.append((query,bot_message))

    return "",chat_history

