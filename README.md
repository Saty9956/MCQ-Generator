# 📚 AI-Powered MCQ Generator (Groq + Streamlit)

An intelligent, high-speed Multiple Choice Question (MCQ) generator powered by the **Groq LPU™ Inference Engine** and **Streamlit**. This tool allows users to upload technical documents (PDF/TXT) or select specific subjects to generate high-quality assessment questions instantly using the `mixtral-8x7b-32768` model.

---

## 🚀 Key Features

* **Multi-Source Input:** Extract content from **PDFs** and **Text files** or generate questions based on pre-defined subjects.
* **Blazing Fast Inference:** Leverages Groq's LPU architecture for near-instantaneous text generation.
* **Customizable Assessments:** Select the number of questions (5-50) and difficulty levels (Easy, Medium, Hard).
* **Clean UI:** Built with Streamlit for a seamless, interactive user experience.
* **Robust Error Handling:** Includes defensive logic for PDF parsing and API communication.

---

## 🛠️ Tech Stack

| Technology        | Purpose                                       |
| :---------------- | :-------------------------------------------- |
| **Python**        | Core logic & scripting                        |
| **Streamlit**     | Frontend UI & file handling                   |
| **Groq API**      | Large Language Model (Mixtral-8x7b) inference |
| **PyPDF2**        | PDF text extraction                           |
| **Python-Dotenv** | Secure environment variable management        |

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Saty9956/MCQ-Generator.git
cd MCQ-Generator
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory and add your Groq API Key:

```
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Run the Application

```bash
streamlit run app.py
```

---

## 📖 How It Works

**Extraction Layer:** The app uses PyPDF2 to strip text from uploaded documents.

**Prompt Engineering:** A structured prompt is sent to the Mixtral model, enforcing a strict JSON-like format (Question, Options, Answer).

**Inference:** Groq processes the context and returns the generated MCQs.

**Presentation:** Streamlit renders the output in a clean, readable format.

---

## 🧠 Architectural Tradeoffs & Enterprise Scaling
While this pipeline is highly functional for mid-sized documents, injecting the entire extracted text directly into the prompt context window has limitations:
* **The Tradeoff:** This guarantees 100% context retention without retrieval loss but caps scalability at the model's token limit (32k tokens). 
* **Enterprise Scaling (Next Steps):** To scale this for 500+ page enterprise documents, this architecture should be upgraded to a **Retrieval-Augmented Generation (RAG)** pipeline (chunking, embedding, and retrieving via Vector DBs like Pinecone/FAISS). Furthermore, migrating from string-based prompt formatting to strict JSON schemas using `Pydantic` and API tool-calling would guarantee deterministic downstream parsing.

## 📂 Project Structure

```
MCQ-Generator/
│
├── app.py                  # Main Streamlit application
├── MCQGenerator.ipynb      # Jupyter Notebook prototype
├── requirements.txt        # Dependencies
├── .env                    # Environment variables (ignored)
└── README.md               # Project documentation
```

---

## 🤝 Contributing

Feel free to fork this repository, open issues, or submit pull requests to improve the parsing logic or add support for more file formats.

---

## 👤 Author

**Satyartha Shukla**
AI/ML Systems Intern @ Intel | M.Tech AI @ NIT Jalandhar
