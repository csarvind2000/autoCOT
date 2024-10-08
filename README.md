
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
    "What is the maximum power output of the Urban Cruiser Hyryder Neodrive E Variant's engine?"
  ],
  "chain_of_thought": "The Urban Cruiser Hyryder Neodrive E Variant has a 1462 cc petrol engine.\n2. The maximum power output of the engine is 75 kW (101.9PS) at 6000 rpm.\n3. This information is provided in the context, and it states that the torque of the engine is 135Nm at 4400 rpm.\n4. Based on the information provided, the maximum power output of the Urban Cruiser Hyryder Neodrive E Variant's engine is 75 kW (101.9PS) at 6000 rpm.\n\nClear and concise answer: The maximum power output of the Urban Cruiser Hyryder Neodrive E Variant's engine is 75 kW (101.9PS) at 6000 rpm.",
  "reflection": "As a meticulous reviewer, I have thoroughly examined the information provided regarding the Urban Cruiser Hyryder Neodrive E Variant's engine specifications. Here is my corrected and improved chain-of-thought reasoning:\n\n1. The Urban Cruiser Hyryder Neodrive E Variant has a 1462 cc petrol engine, delivering a maximum power output of 75 kW (101.9PS) at 6000 rpm and a torque of 135Nm at 4400 rpm.\n2. The engine features a 5-speed manual transmission and a 2WD drive type, providing smooth power delivery and excellent road handling.\n3. In terms of dimensions, the Urban Cruiser Hyryder Neodrive E Variant measures 4365 mm in length, 1795 mm in width, and 1635 mm in height, with a wheelbase of 2600 mm and a turning radius of 5.4 m.\n4. The suspension system consists of MacPherson struts at the front and torsion beams at the rear, providing a comfortable ride and responsive handling.\n5. Braking is facilitated by ventilated discs at the front and solid discs at the rear, ensuring reliable stopping power and safety on the road.\n6. The Urban Cruiser Hyryder Neodrive E Variant rides on steel wheels with full wheel caps, fitted with 215/60 R17 tires for a comfortable ride and excellent grip on various road surfaces.\n7. However, details regarding the hybrid system, battery type and voltage, motor generator type, and total system max power are not provided for this variant.\n8. The exterior features of the Urban Cruiser Hyryder Neodrive E Variant include Bi-Halogen Projector Headlamps, LED Position lamps and Twin LED Day-time running lamps/Side turn lamps, LED Tail Stop Lamps and High mount stop lamps, and Outside Rear View Mirrors (ORVM) with turn indicators.\n9. The variant also features Black wheel arch cladding for both the front and rear, along with Silver Back door garnish and Silver Skid Plates (Front & Rear), giving it a sleek and sporty appearance.\n10. Certain features such as Roof Rails and Front Variable Intermittent wipers are not available, but the variant includes Front Windshield, Front Door, Rear Door, Quarter, and Back Door Green Glass for improved visibility and safety.\n\nBased on the information provided, the maximum power output of the Urban Cruiser Hyryder Neodrive E Variant's engine is 75 kW (101.9PS) at 6000 rpm, with a torque of 135Nm at 4400 rpm. The variant features a 5-speed manual transmission and a 2WD drive type, along with a comprehensive list of exterior features that enhance its performance, comfort, and style.",
  "final_answer": "Based on the reflection provided, the final and refined answer to the question \"What is the maximum power output of the Urban Cruiser Hyryder Neodrive E Variant's engine?\" is:\n\nThe Urban Cruiser Hyryder Neodrive E Variant has a maximum power output of 75 kW (101.9PS) at 6000 rpm, with a torque of 135Nm at 4400 rpm.\n\nThis answer is based on the information provided in points 1 and 2 of the reflection, which states that the engine has a maximum power output of 75 kW (101.9PS) at 6000 rpm and a torque of 135Nm at 4400 rpm. The answer also takes into account the 5-speed manual transmission and 2WD drive type, which are features of the Urban Cruiser Hyryder Neodrive E Variant as stated in points 3 and 4 of the reflection."
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
