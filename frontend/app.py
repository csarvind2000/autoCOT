# frontend/app.py

import streamlit as st
import requests
import json

# Set the FastAPI backend URL
BACKEND_URL = "http://localhost:8000/process-pdf"

def main():
    st.title("PDF Question Generator with CoT and Reflection")
    st.write("Upload a PDF file to generate questions and answers with Chain-of-Thought reasoning and reflection.")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        max_questions = st.number_input("Number of questions to generate", min_value=1, max_value=20, value=5)

        if st.button("Process PDF"):
            with st.spinner("Processing..."):
                files = {'pdf_file': (uploaded_file.name, uploaded_file.getvalue(), 'application/pdf')}
                params = {'max_questions': int(max_questions)}
                try:
                    response = requests.post(BACKEND_URL, files=files, params=params)
                    if response.status_code == 200:
                        results = response.json()
                        st.success("Processing complete!")

                        for idx, res in enumerate(results):
                            st.subheader(f"Question {idx + 1}: {res['question']}")
                            with st.expander("Chain of Thought"):
                                st.write(res['chain_of_thought'])
                            with st.expander("Reflection"):
                                st.write(res['reflection'])
                            st.write(f"**Final Answer:** {res['final_answer']}")
                            st.write("---")

                        # Option to download the results as JSON
                        json_results = json.dumps(results, indent=2)
                        st.download_button(
                            label="Download Results as JSON",
                            data=json_results,
                            file_name='results.json',
                            mime='application/json'
                        )
                    else:
                        st.error(f"Error: {response.json()['detail']}")
                except Exception as e:
                    st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
