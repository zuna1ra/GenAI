# 🤖 Local LLM Chatbot

A Streamlit-based chatbot that connects to locally hosted Large Language Models (LLMs) using Ollama, enabling private AI conversations without relying on cloud services.

## Features

* Interactive chat interface built with Streamlit
* Support for multiple LLMs through Ollama
* Chat history management
* Adjustable temperature settings
* Download chat conversations
* Custom UI styling
* Local AI inference without cloud dependencies

## Technologies Used

* Python
* Streamlit
* Ollama
* Requests

## Project Structure

Local LLM Chatbot/

├── app.py

├── requirements.txt

└── README.md

## Installation

1. Clone the repository:

```bash
git clone https://github.com/zuna1ra/GenAI.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start Ollama and ensure a model is available.

4. Run the application:

```bash
streamlit run app.py
```

## Supported Models

* Gemma 2B
* Llama 3
* Mistral

## Future Improvements

* Voice input support
* PDF export
* RAG integration
* User authentication
* Chat search functionality

## Author

Zunaira Sohail
