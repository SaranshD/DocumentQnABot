# QnA Bot for PDFs

A simple Retrieval-QA pipeline that lets you query reasonably sized PDFs (like textbook chapters or research papers) using a local LLM (via [Ollama](https://ollama.ai/)) and vector search.

## Features
- Loads PDFs and segments text into structured documents
- Creates embeddings using HuggingFace models
- Stores embeddings in a local ChromaDB vector store
- Uses Ollama (e.g., Gemma3:1B) as the LLM backend
- Lets you ask natural language questions about the PDF

---

## Requirements
- Python 3.9+
- [Ollama](https://ollama.ai/) installed and running
- A supported model pulled (e.g. `ollama pull gemma3:1b`)

---

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/my-qna-bot.git
   cd my-qna-bot
2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS\Linux
   source venv\bin\activate
3. Install dependencies
   ```bash
   pip install -r requirements.txt
4. Place your PDF file in the project root (like sample.pdf)

---

## Usage

Run the QnA pipeline
```bash
python qna_pipeline.py
```
By default, the script loads sample.pdf, indexes it, and allows you to ask questions like:
```
"Explain everything about classes in this document"
```

---

## License

This project is open source (MIT). See [LICENSE](LICENSE) for details.
