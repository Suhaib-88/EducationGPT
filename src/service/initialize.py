import os
import gradio as gr


def set_env(model,access_info):
    if not access_info:
        return gr.update(value="Token Not found")

    os.environ['MODEL']= model
    if model == "gemini":
        os.environ["GOOGLE_API_KEY"]=access_info
    
    elif model=='groq':
        os.environ["GROQ_API_KEY"]=access_info

    return gr.update(value="token updated successfully ✅")
    

    