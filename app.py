from transformers import pipeline
import gradio as gr

model = pipeline("summarization", model="google-t5/t5-small")


def predict(prompt:str):
    summary = model(prompt)[0]['summary_text']
    return summary

with gr.Blocks() as txtsm:
    textbox = gr.Textbox(placeholder="Enter text block to summarize", lines=4)
    gr.Interface(fn=predict, inputs=textbox, outputs="text")


txtsm.launch()
