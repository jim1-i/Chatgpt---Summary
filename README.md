# ChatGPT Text Summarizer

A simple Python project that summarizes the main idea of a `.txt` article using OpenAI's ChatGPT.

## Features

- Command-line mode to summarize `.txt` files
- Gradio UI mode to upload and summarize files visually
- Loads API key from the environment variable `OPENAI_API_KEY`

## Setup

1. Install dependencies:
```bash
pip install openai gradio

2. Set your OpenAI API key
```bash
export OPENAI_API_KEY=your_openai_key   # for Linux/macOS
set OPENAI_API_KEY=your_openai_key      # for Windows CMD

3.1 Run program by UI
```bash
python ui.py

3.2 Run program by command line
```bash
python main.py --file ../test/test.txt --output ../test/summary.txt

