# 🏥 A Medical Document Conversational Framework Using MedGemma  
### Reliable Cancer Screening Assistance using RAG + GenAI

---

## 1️⃣ Introduction  
This project presents a **medical document conversational AI system** that assists users in understanding cancer screening related medical reports.  
By combining **MedGemma (a medical domain Large Language Model)** with **Retrieval-Augmented Generation (RAG)**, the system provides **document-grounded answers** to user queries.  
The goal is to help users explore medical documents in a safe, explainable, and reliable manner for **educational purposes**.

> ⚠️ This is an academic project and not a medical diagnosis tool.

---

## 2️⃣ Overview  
The system allows users to upload medical documents (PDF, DOCX, images) and ask questions related to cancer screening.  
The workflow includes:
- Extracting text from documents (OCR + parsers)  
- Splitting content into chunks  
- Creating embeddings for retrieval  
- Fetching relevant context using FAISS  
- Generating responses using **MedGemma**  

This follows the **RAG architecture** to reduce hallucinations and improve answer reliability.

---

## 3️⃣ Demos  
### 🧱 Architecture Diagram 
