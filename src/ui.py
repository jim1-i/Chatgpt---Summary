import gradio as gr
from backend import summarize_text

def summarize_uploaded_file(file):
    content = file.decode("utf-8")
    return summarize_text(content)

def launch_gradio_app():
    gr.Interface(
        fn=summarize_uploaded_file,
        inputs=gr.File(label="Upload a TXT File", type="binary"),
        outputs="text",
        title="ChatGPT Main Idea Summarizer",
        flagging_mode="never"
    ).launch()

if __name__ == "__main__":
    launch_gradio_app()
