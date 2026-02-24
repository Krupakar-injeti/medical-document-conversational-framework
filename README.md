# 🏥 A Medical Document Conversational Framework Using MedGemma  
### Reliable Cancer Screening Assistance using MEDGemma + GenAI

A GenAI-powered medical document chatbot that helps users understand cancer screening related medical reports using **MedGemma (Google’s medical LLM)** and **Retrieval-Augmented Generation (RAG)**.

> ⚠️ Academic project for educational purposes only. Not a medical diagnosis system.

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)  
![GenAI](https://img.shields.io/badge/GenAI-MedGemma-purple)  
![RAG](https://img.shields.io/badge/Architecture-RAG-orange)  

---

## 1️⃣ Introduction  
Medical reports are often difficult for non-experts to understand. This project builds a **medical document conversational AI system** that allows users to upload medical reports (PDFs, scanned images, DOCX) and ask questions related to **cancer screening**.  

By combining **document retrieval** with **MedGemma**, the system generates **context-aware and reliable answers** grounded in the uploaded medical content.

---

## 2️⃣ Overview  
The system follows a **Retrieval-Augmented Generation (RAG)** pipeline:

- User uploads a medical document  
- Text is extracted using PDF parsers and OCR  
- Document is split into chunks  
- Relevant chunks are retrieved using embeddings + FAISS  
- MedGemma LLM generates an answer using retrieved context  
- The response is delivered in a patient-friendly format  

This approach reduces hallucinations and improves trustworthiness.

---

## 3️⃣ Demos  

### 🧱 Architecture  
![Architecture](assets/architecture.jpg)

**Pipeline:**  
User → Query Understanding → Document Retrieval → RAG Integration (MedGemma) → Answer Synthesis → Result Delivery

---

### 🎥 Demo Video  

<video width="700" controls>
  <source src=
</video>

## 📂 Project Structure

```text
medical-document-conversational-framework/
├── medgemma.py        # Loads MedGemma model
├── file_loader.py    # File loaders (PDF, DOCX, Images)
├── ocr.py            # OCR utilities (PyTesseract)
├── embeddings.py     # Embedding model loader
├── retriever.py      # Text chunking logic
├── vectorstore.py    # FAISS vector store
├── store.py          # LangChain FAISS store
├── app.py            # Main application (CLI / Streamlit-ready)
├── assets/
│   └── architecture.jpg
├── README.md
└── .gitignore

---

## 5️⃣ Deployed / Run Locally  

- ✅ Run Locally / Google Colab  
- ❌ Not deployed publicly (medical model + GPU constraints)  
- 🔮 Can be deployed on Streamlit Cloud / Hugging Face Spaces in future  

---

## 6️⃣ Deployment Guide (Google Colab)

### 🔧 Install Dependencies  
```bash
pip install -U torch transformers accelerate sentence-transformers langchain faiss-cpu pytesseract pillow python-dotenv streamlit pdfplumber pymupdf python-docx pandas
🔐 Set HuggingFace Token (Secure)
from google.colab import userdata
userdata.set("HUGGINGFACEHUB_API_TOKEN", "YOUR_TOKEN")

❌ Do NOT hardcode tokens in code or push them to GitHub.

▶️ Run
python app.py
7️⃣ Tech Stack

Language: Python

LLM: MedGemma (google/medgemma-1.5-4b-it)

Frameworks: Hugging Face Transformers, LangChain

Vector DB: FAISS

Embeddings: Sentence Transformers

OCR: PyTesseract

PDF Parsing: PDFPlumber, PyMuPDF

Frontend (Optional): Streamlit

Platform: Google Colab / Local

📌 Conclusion

This project demonstrates how GenAI + RAG can be applied to medical document understanding for reliable cancer screening assistance. The architecture ensures answers are grounded in source documents, improving explainability and trust.

👨‍🎓 Author

Final Year B.Tech (AI & DS)
India
