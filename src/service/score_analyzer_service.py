import gradio as gr
from src.utils.score_analyzer import ScoreAnalyzer


def update_result(choice):
    if choice ==0:
        return[gr.update(visible=True), gr.update(visible=False)]
    if choice==1:
        return[gr.update(visible=False), gr.update(visible=True)]
    

def execute_score_analyzer(desc:str, file_, choice:int):
    if desc is None:
        raise gr.Error("Please enter analysis objective")
    if file_ is None:
        raise gr.Error("Please upload the file")
    
    try:
        file_name=str(file_.name).replace("\\",'/')
        score_analyzer= ScoreAnalyzer(file_name)
        if choice==0:
            result= score_analyzer.plot_df(desc)
            codeblocks=result["codeblocks"]
            exec(codeblocks,globals(),locals())
            func= eval('chart_plot()',globals(),locals())
            return [gr.update(value=func), gr.update()]
        if choice==1:
            result= score_analyzer.chat_with_data(desc)
            return [gr.update(),gr.update(value=result)     ]
    except Exception as e:
        raise gr.Error(e)