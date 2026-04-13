# Define the Streamlit app code content for app.py
app_code = '''
import os
import streamlit as st
from groq import Groq
import PyPDF2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def extract_text_from_pdf(file_bytes):
    """Extract text from a PDF file."""
    try:
        reader = PyPDF2.PdfReader(file_bytes)
        text = "\\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
        return text
    except Exception as e:
        st.error("Error reading PDF: " + str(e))
        return ""

def extract_text_from_txt(file_bytes):
    """Extract text from a TXT file."""
    try:
        return file_bytes.read().decode('utf-8')
    except Exception as e:
        st.error("Error reading text file: " + str(e))
        return ""

def main():
    st.title("📚 MCQ Generator using Groq API")

    uploaded_file = st.file_uploader("📂 Upload a PDF or TXT file (optional)", type=["pdf", "txt"])
    
    subjects = ["Mathematics", "Physics", "Chemistry", "Biology", "History", "Geography", "Computer Science", "Artificial Intelligence", "Machine Learning"]
    selected_subject = st.selectbox("📖 Select Subject (if no file is provided)", subjects)
    
    num_questions = st.slider("🔢 Select Number of MCQs", min_value=5, max_value=50, value=10)
    
    difficulty = st.selectbox("🎯 Select Difficulty Level", options=["easy", "medium", "hard"])

    if st.button("🚀 Generate MCQs"):
        content_text = ""
        
        if uploaded_file:
            file_ext = os.path.splitext(uploaded_file.name)[1].lower()
            if file_ext == ".pdf":
                content_text = extract_text_from_pdf(uploaded_file)
            elif file_ext == ".txt":
                content_text = extract_text_from_txt(uploaded_file)
            else:
                st.error("Unsupported file format.")
                return

        elif selected_subject:
            content_text = f"Generate {num_questions} MCQs for the subject: {selected_subject}."

        if content_text:
            st.subheader("🔍 Extracted Text Preview")
            st.text(content_text[:500])
            
            prompt = f"""
You are an MCQ generator. Create {num_questions} multiple-choice questions based on the content provided.
Difficulty level: {difficulty}
Content:
{content_text}
Format:
Question: <question text>
A) <option A>
B) <option B>
C) <option C>
D) <option D>
Answer: <correct option>
"""

            # Get the API key from the environment variables
            api_key = os.getenv("GROQ_API_KEY")
            if not api_key:
                st.error("❌ API Key is missing! Please set the API key in the .env file.")
                return

            client = Groq(api_key=api_key)

            try:
                chat_completion = client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model="mixtral-8x7b-32768",
                    stream=False,
                )
                mcq_output = chat_completion.choices[0].message.content
                st.subheader("✅ Generated MCQs")
                st.text(mcq_output)
            except Exception as e:
                st.error("Error generating MCQs: " + str(e))
        else:
            st.error("❌ Please upload a file or select a subject.")

if __name__ == "__main__":
    main()
'''

# Write the app code to a new file app.py
with open("app.py", "w", encoding="utf-8") as f:
    f.write(app_code)

# Confirm that the app.py file has been created
print("✅ app.py file created successfully!")
