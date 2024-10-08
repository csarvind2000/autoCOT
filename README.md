
# autoCOT: Automated Chain of Thought with Reflection

`autoCOT` is an automated system for generating Chain of Thought (CoT) reasoning with reflection, designed for processing custom datasets or PDF documents. The system uses **FastAPI** for serving the pipeline and integrates with **LLaMA2-13b** via **Ollama** or **LiteLLM** to generate questions, answers, and reflections. The goal is to improve the quality of reasoning by automating prompt refinement and providing insights.

## Features

- **PDF Upload & Text Extraction**: Upload PDF documents for automatic text extraction.
- **Chain of Thought (CoT)**: Generate detailed CoT reasoning for documents.
- **Reflection Mechanism**: Review and refine reasoning to improve accuracy.
- **FastAPI & Streamlit**: Access the service via a REST API or a simple Streamlit interface.
- **Customizable Models**: Use LLaMA2-13b locally via Ollama or LiteLLM.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [How It Works](#how-it-works)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.12.3
- Conda (optional)
- pip

### Step-by-Step Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/autoCOT.git
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

4. **Set up environment variables for LLaMA2-13b:**

   Since you're using **LLaMA2-13b** with **Ollama** or **LiteLLM**, ensure that the model is installed and set up locally. You don’t need an OpenAI API key for this setup.

   1. **Install the LLaMA2-13b model** via **Ollama**:

      ```bash
      ollama pull llama2:13b
      ```

   2. **Start the LiteLLM server** with the LLaMA model:

      ```bash
      litellm serve --model llama2:13b-chat
      ```

   Make sure your **LiteLLM** server is running so that it can handle requests from the **FastAPI** app.

5. **Run the FastAPI server:**

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

6. **Access the API:**

   The API will be accessible at `http://localhost:8000`.

---

## Usage

### 1. FastAPI API

After starting the server, you can upload a PDF and receive the Chain of Thought (CoT) reasoning and reflection in JSON format.

#### Upload a PDF

Send a POST request to upload a PDF file:

```bash
curl -X POST "http://localhost:8000/process-pdf" -F "pdf_file=@your_file.pdf"
```

The server will return a JSON response containing generated questions, answers, CoT reasoning, and reflections.

### 2. Streamlit Interface

You can interact with the service via the Streamlit interface by running:

```bash
streamlit run app.py
```

Upload a PDF through the UI, and you will receive a JSON response with CoT and reflection.

---

## API Endpoints

### `POST /process-pdf`

- **Description**: Upload a PDF document for text extraction, question generation, CoT reasoning, and reflection.
- **Parameters**: `pdf_file` (file)
- **Response**: A JSON object containing the extracted text, generated questions, CoT reasoning, reflection, and final answers.

Example response:

```json
{
  "questions": ["What is the main theme of the document?"],
  "chain_of_thought": "Step-by-step reasoning based on the content...",
  "reflection": "Reflecting on the CoT, improvements were made by...",
  "final_answer": "Final refined answer after reflection."
}
```

---

## How It Works

1. **PDF Upload & Text Extraction**: The user uploads a PDF file. The system extracts text using **pdfplumber** for further processing.
2. **Question Generation**: Agents automatically generate questions based on the document’s content.
3. **Chain of Thought Reasoning**: The system performs step-by-step reasoning for answering the generated questions.
4. **Reflection**: A reflection step is performed on the initial reasoning to improve accuracy and provide a more refined answer.

### Models Supported

- **LLaMA2-13b**: Integrated using **Ollama** or **LiteLLM** to run locally for CoT reasoning and reflection.

---

## Examples

Here’s an example of how to interact with the FastAPI service via a terminal:

### Uploading a PDF and Getting a Response

```bash
curl -X POST "http://localhost:8000/process-pdf" -F "pdf_file=@example.pdf"
```

Example JSON response:

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

## Contributing

We welcome contributions to improve **autoCOT**. Here’s how you can contribute:

1. **Fork the repository** on GitHub.
2. **Create a new branch** for your feature or bug fix.
3. **Submit a pull request** to the `main` branch.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
