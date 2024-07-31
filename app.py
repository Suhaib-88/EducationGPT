import gradio as gr
import pandas as pd
from src.service.initialize import set_env
from src.service.score_analyzer_service import execute_score_analyzer,update_result

with gr.Blocks(theme= gr.themes.Soft()) as demo:
    gr.Markdown("Welcome to EducationGPT")
    gr.Markdown("Accessible education AI tool for all")

    with gr.Tab("Homepage"):
        gr.Markdown("please make sure you have set in the right api token first")
        with gr.Row():
            with gr.Column():
                model= gr.Radio(choices=['gemini','groq'], label='model selection', value="gemini",interactive=True)
                access_info= gr.Textbox(label='Enter your api key/token')

            with gr.Column():
                info= gr.Label(value='State: not set',show_label=False)
                

        gr.Button("Confirm").click(fn=set_env,inputs=[model,access_info],outputs=info)


    """
    Teacher Grade Analyst
    """
    with gr.Tab("Grade Analyst"):
        gr.Markdown("Intelligent Grade Analyst")
        gr.Markdown("Upload transcript to be analysted")
        with gr.Row():
            file= gr.File(label="upload files", file_types=[".csv"])

        with gr.Row():
            frame= gr.DataFrame(
                wrap= True,
                label="Transcript",
                type='pandas',
                visible= False
                
            )

            file.upload(fn= lambda value: gr.DataFrame.update(value=pd.read_csv(str(value.name)),visible=True),
                        inputs=file,
                        outputs=frame,
                        show_progress=True)
            file.clear(fn= lambda: gr.DataFrame.update(value=None, visible=False), outputs= frame)

        
        gr.Markdown("## Analyse the results")
        with gr.Row(equal_height= True):
            analyzer_plot= gr.Plot(label="Image Analysis", show_label= True)
            analyzer_textbox= gr.Textbox(label="Data Exploration", show_label=True, lines=8, visible=False)

        gr.Markdown("## Analsis settings")
        with gr.Row():
            dimension= gr.Radio(
                choices= ["Image analysis", "Data Exploration"],
                label="Analytical method",
                type='index',
                value="Image analysis",
                interactive= True
            )
            dimension.change(fn=update_result,inputs=dimension,outputs=[analyzer_plot,analyzer_textbox])

            desc_input= gr.Textbox(placeholder="Enter the data you want to obtain, for example: Display the highest and lowest scores of all Tests",
                                   label="Analysis objectives",)
            analyzer_button= gr.Button(value= "start Analysis",variant= "primary")
            if desc_input is not None:
                analyzer_button.click(fn=execute_score_analyzer,inputs=[desc_input,file, dimension],outputs=[analyzer_plot,analyzer_textbox])
            else:
                gr.Info('Please enter the analysis objective first.')
    
    """
    Online course summary
    """
    with gr.Tab("Online Course Summary"):
        gr.Markdown("## Online Course Summary")
        with gr.Row(equal_height=True):
            with gr.Column():
                bv_input= gr.Textbox(placeholder="Please Enter the video link for which you want to generate a summary",
                                     label="",
                                     value="",
                                     interactive=True,
                                     max_lines=4)
                
                p_input= gr.Textbox(placeholder="Please enter the sub-p number",
                                    label= "enter the sub number",
                                    value="0",
                                    interactive=True,
                                    max_lines=4)
                summary_button= gr.Button('Start summary')

                with gr.Box():
                    with gr.Box():
                        gr.Markdown('# Q&A bot')
                        chatbot= gr.Chatbot(labve="AI Answer")
                        qa_input= gr.Textbox(label="Chat with video", interactive= True, placeholder= "Enter your question here")

                        with gr.Row():
                            clear= gr.ClearButton([qa_input,chatbot],value_="clear")
                            send_button= gr.Button(value="send")

            with gr.Column():
                info_output= gr.Textbox(interactive=False,lines=25,label= "Video subtitles", show_label=True)
                summary_output=gr.Textbox(interactive=False, lines=10,label= "AI summarize", show_label=True)

                summary_button.click(fn= create_summary, inputs=[bv_input,p_input], outputs=[info_output, summary_output])
                send_button.click(fn=generate_qa,inputs=[info_output,qa_input,chatbot],outputs=[qa_input,chatbot])





if __name__=='__main__':
    demo.launch()