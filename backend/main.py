# backend/main.py

import os
import json
import pdfplumber
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from typing import List, Dict
import aiofiles
import requests  # Added for HTTP requests to Ollama
import time

app = FastAPI(title="PDF Processing API")

# Ollama settings
OLLAMA_URL = 'http://localhost:11434'  # Adjust if your Ollama server runs on a different port
MODEL_NAME = 'llama2:13b-chat'  # Use one of the models you have installed, e.g., 'llama2:13b-chat'

# Functions used by agents

async def extract_text_from_pdf(pdf_file: UploadFile) -> str:
    """Extracts text from an uploaded PDF file."""
    try:
        async with aiofiles.open(pdf_file.filename, 'wb') as out_file:
            content = await pdf_file.read()
            await out_file.write(content)
        text = ""
        with pdfplumber.open(pdf_file.filename) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        os.remove(pdf_file.filename)  # Clean up the file after processing
        return text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing PDF: {e}")

def ollama_generate(prompt: str, model: str = MODEL_NAME) -> str:
    """Generates a response from the local LLM via Ollama."""
    url = f'{OLLAMA_URL}/api/generate'

    payload = {
        'model': model,
        'prompt': prompt,
    }

    try:
        response = requests.post(url, json=payload, stream=True)
        response.raise_for_status()

        # Collect the response stream
        generated_text = ''
        for line in response.iter_lines():
            if line:
                line = line.decode('utf-8')
                data = json.loads(line)
                if 'done' in data and data['done']:
                    break
                if 'response' in data:
                    generated_text += data['response']
        return generated_text.strip()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error communicating with Ollama: {e}")

def generate_questions_agent(context: str, max_questions: int = 5) -> List[str]:
    """Generates questions based on the provided context using a local LLM."""
    prompt_template = f"""You are an AI assistant that generates insightful questions from a text.

Text:
\"\"\"
{context}
\"\"\"

Generate {max_questions} questions that cover the key points of the text.

Questions:"""

    prompt = prompt_template

    # Call the local LLM via Ollama
    try:
        response_text = ollama_generate(prompt)
        questions = response_text.strip().split('\n')
        questions = [q.strip('- ').strip() for q in questions if q.strip()]
        return questions
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating questions: {e}")

def generate_cot_agent(question: str, context: str) -> str:
    """Generates an answer with chain-of-thought reasoning using a local LLM."""
    prompt_template = f"""You are a knowledgeable assistant.

Please follow these steps:

1. Read the question carefully.
2. Recall relevant information from the context.
3. Explain your reasoning step-by-step.
4. Provide a clear and concise answer at the end.

Context:
{context}

Question:
{question}

Chain-of-thought reasoning:"""

    prompt = prompt_template

    try:
        response_text = ollama_generate(prompt)
        return response_text.strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating chain-of-thought: {e}")

def reflection_agent(question: str, context: str, chain_of_thought: str) -> str:
    """Performs reflection on the chain-of-thought reasoning using a local LLM."""
    prompt_template = f"""You are a meticulous reviewer.

Please follow these steps:

1. Review the initial chain-of-thought reasoning for accuracy and completeness.
2. Identify any errors, omissions, or areas for improvement.
3. Provide a corrected and improved chain-of-thought reasoning.
4. Ensure the final answer is clear and accurate.

Context:
{context}

Question:
{question}

Initial chain-of-thought reasoning:
{chain_of_thought}

Reflection:"""

    prompt = prompt_template

    try:
        response_text = ollama_generate(prompt)
        return response_text.strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during reflection: {e}")

def extract_final_answer_agent(reflection: str) -> str:
    """Extracts the final answer from the reflection using a local LLM."""
    prompt = f"""Based on the reflection below, provide the final, refined answer.

Reflection:
{reflection}

Answer:"""

    try:
        response_text = ollama_generate(prompt)
        return response_text.strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error extracting final answer: {e}")

def process_question(question: str, context: str) -> Dict:
    """Processes a single question through CoT and reflection agents."""
    # Generate chain-of-thought reasoning
    chain_of_thought = generate_cot_agent(question, context)

    # Perform reflection
    reflection = reflection_agent(question, context, chain_of_thought)

    # Extract final answer
    final_answer = extract_final_answer_agent(reflection)

    # Prepare the result
    result = {
        'question': question,
        'chain_of_thought': chain_of_thought,
        'reflection': reflection,
        'final_answer': final_answer
    }

    return result

def process_context(context: str, max_questions: int = 5) -> List[Dict]:
    """Processes the context and returns the results."""
    # Limit context length if necessary
    max_context_length = 2000  # Adjust as needed
    context = context[:max_context_length]

    # Generate questions
    questions = generate_questions_agent(context, max_questions)

    results = []

    # Process each question
    for idx, question in enumerate(questions):
        print(f"Processing question {idx + 1}/{len(questions)}: {question}")
        result = process_question(question, context)
        results.append(result)

    return results

# FastAPI endpoint
@app.post("/process-pdf")
async def process_pdf_endpoint(pdf_file: UploadFile = File(...), max_questions: int = 5):
    """Endpoint to process the uploaded PDF and return the results."""
    if pdf_file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a PDF file.")

    try:
        # Extract text from PDF
        context = await extract_text_from_pdf(pdf_file)

        # Process the context
        results = process_context(context, max_questions)

        # Return the results as JSON
        return JSONResponse(content=results)

    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
