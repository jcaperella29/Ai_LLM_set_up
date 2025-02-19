# Ai_LLM_set_up


# AI LLM Paper Summarizer with Ollama

## Overview
This project automates the extraction and summarization of research papers using **Local Large Language Models (LLMs)** via **Ollama**. It processes **scientific PDFs**, extracts relevant text, and generates structured summaries for each section.

## Features
- 📄 **Extracts text from scientific PDFs**
- 🤖 **Summarizes research papers using Ollama** (Mistral, Gemma, or LLaMA models)
- 🏗️ **Processes large documents in chunks** for better accuracy
- 🔍 **Identifies key topics in life sciences & bioinformatics**

## Setup Instructions
### 1️⃣ Install Dependencies
First, make sure you have Python installed. Then install the required libraries:
```sh
pip install pymupdf requests
```

### 2️⃣ Install & Run Ollama
Download and install **Ollama** from [Ollama's website](https://ollama.com).
Start the Ollama server:
```sh
ollama serve
```
To use a lighter model, install **Gemma** or **Mistral**:
```sh
ollama pull gemma
ollama pull mistral
```

### 3️⃣ Run the Script
Activate the virtual environment (if using one):
```sh
cd path/to/project
.\venv\Scripts\Activate  # On Windows
```
Then execute the script:
```sh
python LLM_test.py
```

## Optimization Options
- Reduce **chunk size** (from 3000 to 1500 characters) for faster processing.
- Use **lighter models** like `gemma` for better speed.
- Adjust **Ollama's thread settings** for better CPU performance:
  ```sh
  OLLAMA_NUM_THREADS=8 ollama serve
  ```

## Next Steps
- 📌 **Citation & Figure Extraction** (Upcoming Feature)
- ⚡ **Parallel Processing** to speed up large document analysis
- 🌐 **Cloud Integration** for faster summaries with OpenAI API

## Contributing
Feel free to fork the repo, submit issues, or suggest improvements!

## License
MIT License - Free to use and modify!

