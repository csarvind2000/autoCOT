
# 🚀 autoCOT: Automated Chain of Thought with Reflection 🤖

`autoCOT` is an intelligent system powered by **agents**, built to automate **Chain of Thought (CoT)** reasoning with reflective feedback for PDF documents or custom datasets. This system utilizes **FastAPI** for backend services and **LLaMA2-13b** via **Ollama** or **LiteLLM** to generate questions, CoT reasoning, and reflective answers. The core idea is to automate reasoning processes while refining and improving the quality of the answers through **reflection**.

---

## 🌟 Features

- 📝 **PDF Upload & Text Extraction**: Automatically extract text from uploaded PDFs.
- 💡 **Chain of Thought (CoT) Reasoning**: Use agents to generate detailed CoT reasoning for various topics.
- 🔍 **Reflection Mechanism**: Enhance answers by reviewing and refining initial CoT reasoning, resulting in more accurate and thoughtful answers.
- ⚡ **FastAPI & Streamlit Integration**: The system is accessible through a **FastAPI** REST API and a simple-to-use **Streamlit** interface.
- 🔧 **Customizable Models**: Utilize **LLaMA2-13b** locally through **Ollama** or **LiteLLM** for efficient reasoning and reflection.

---

## ⚙️ Installation

### 📋 Prerequisites

- Python 3.12.3
- Conda (optional, recommended)
- pip
- **Ollama** for model handling

### Step-by-Step Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/csarvind2000/autoCOT.git
   cd autoCOT
   ```

2. **Create and activate a virtual environment:**

   Using Conda:

   ```bash
   conda create --name autoCOT python=3.12.3
   conda activate autoCOT
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment for LLaMA2-13b:**

   Since you're using **LLaMA2-13b** with **Ollama** or **LiteLLM**, ensure the model is installed and running locally.

   - **Install the LLaMA2-13b model** via **Ollama**:

     ```bash
     ollama pull llama2:13b
     ```

   - **Start the LiteLLM server**:

     ```bash
     litellm serve --model llama2:13b-chat
     ```

   Ensure your **LiteLLM** or **Ollama** server is running for FastAPI to communicate with it.

5. **Run the FastAPI server:**

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

6. **Access the API:**

   The FastAPI backend will be available at `http://localhost:8000`.

---

## 🕹️ Usage

### 1. **FastAPI API (via Curl or Postman)**

Upload a PDF file and generate Chain of Thought (CoT) reasoning, reflection, and final refined answers via a POST request.

#### Upload a PDF

```bash
curl -X POST "http://localhost:8000/process-pdf" -F "pdf_file=@your_file.pdf"
```

This will return a JSON response containing extracted questions, CoT reasoning, reflections, and refined answers.

### 2. **Streamlit Interface**

Alternatively, interact with the system using a visual interface. Run the **Streamlit** app:

```bash
streamlit run frontend/app.py
```

Upload a PDF file through the Streamlit UI and visualize the generated reasoning and answers.

---

## 🔥 API Endpoints

### `POST /process-pdf`

- **Description**: Upload a PDF for text extraction, question generation, CoT reasoning, and reflection.
- **Parameters**: `pdf_file` (file), `max_questions` (int, optional, default: 5)
- **Response**: A JSON object containing the extracted text, generated questions, CoT reasoning, reflection, and final answers.

Example JSON response:

```json
{
  "questions": ["What is the main argument presented in the document?"],
  "chain_of_thought": "Step-by-step reasoning for the argument...",
  "reflection": "Improved reasoning after reflection...",
  "final_answer": "Final answer after reflection."
}
```

---

## 🧠 How It Works

1. **PDF Upload & Text Extraction**: Users upload PDF files, and the system extracts text using **pdfplumber**.
2. **Agents for Every Task**:
   - **Extraction Agent**: Extracts text from the uploaded PDF.
   - **Question Generation Agent**: Automatically generates insightful questions based on the text.
   - **CoT Reasoning Agent**: Provides step-by-step reasoning for answering each generated question.
   - **Reflection Agent**: Reviews the CoT reasoning and suggests improvements.
3. **Final Answer Generation**: After reflection, the system provides a refined final answer to each question.

### 🛠 Models Supported

- **LLaMA2-13b** via **Ollama** or **LiteLLM** to perform reasoning and reflection efficiently, all processed locally.

---

## 🖼 Examples

### Uploading a PDF via API

```bash
curl -X POST "http://localhost:8000/process-pdf" -F "pdf_file=@example.pdf"
```

Example JSON output:

```json
{
  "questions": [
    "What is the main contribution of the research?"
  ],
  "chain_of_thought": "The main contribution of the research is...",
  "reflection": "Upon review, the contribution can be further clarified...",
  "final_answer": "The clarified contribution of the research is..."
}
```

---

## 🙌 Contributing

We welcome all contributions to improve **autoCOT**! Whether you're fixing a bug, adding a feature, or optimizing performance, follow these steps:

1. **Fork the repository**.
2. **Create a new branch** for your feature or fix.
3. **Submit a pull request** to the `main` branch for review.

---

## 📄 License

This project is licensed under the **MIT License**. For more details, see the [LICENSE](LICENSE) file.

---

## 💡 Ideas for Future Enhancements

- 💻 **Support for More Models**: Add support for different LLaMA models or other local models.
- ⚙️ **Integration with GPT-4**: Provide an option to switch between local models and GPT-4 for improved reasoning.
- 🌐 **Multilingual Support**: Allow PDF documents in multiple languages and handle CoT reasoning across languages.

---

## 🎯 Powered by Intelligent Agents

This system is built on **agent-based architecture** where each agent has a specific role—text extraction, question generation, reasoning, and reflection—working together to produce high-quality results.
