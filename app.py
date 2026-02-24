%%writefile app.py
import os
import io
import json
import csv
import xml.etree.ElementTree as ET

import torch
import pdfplumber
from docx import Document
from PIL import Image
import pytesseract

from medgemma import load_medgemma, generate_response


# -----------------------------
# CONFIG
# -----------------------------
MAX_INPUT_CHARS = 2000
MAX_NEW_TOKENS = 64


# -----------------------------
# Helpers
# -----------------------------
def truncate_text(text):
    return text[:MAX_INPUT_CHARS] if text else ""


def extract_text_any_file(file_path):
    filename = file_path.lower()

    with open(file_path, "rb") as f:
        raw = f.read()

    try:
        if filename.endswith(".txt"):
            return raw.decode("utf-8", errors="ignore")

        if filename.endswith(".pdf"):
            text = ""
            with pdfplumber.open(io.BytesIO(raw)) as pdf:
                for page in pdf.pages:
                    if page.extract_text():
                        text += page.extract_text() + "\n"
            return text

        if filename.endswith(".docx"):
            doc = Document(io.BytesIO(raw))
            return "\n".join(p.text for p in doc.paragraphs)

        if filename.endswith((".csv", ".tsv")):
            sep = "," if filename.endswith(".csv") else "\t"
            reader = csv.reader(
                raw.decode("utf-8", errors="ignore").splitlines(),
                delimiter=sep,
            )
            return "\n".join(" | ".join(row) for row in reader)

        if filename.endswith(".json"):
            obj = json.loads(raw.decode("utf-8", errors="ignore"))
            return json.dumps(obj, indent=2)

        if filename.endswith(".xml"):
            tree = ET.fromstring(raw)
            return ET.tostring(tree, encoding="unicode")

        if filename.endswith((".png", ".jpg", ".jpeg", ".bmp", ".tiff")):
            img = Image.open(io.BytesIO(raw))
            return pytesseract.image_to_string(img)

        return raw.decode("utf-8", errors="ignore")

    except Exception as e:
        return f"[ERROR reading file: {e}]"


# -----------------------------
# MAIN
# -----------------------------
def main():
    print("🔄 Loading MedGemma model...")
    tokenizer, model = load_medgemma()
    model.eval()
    torch.set_grad_enabled(False)

    file_path = input("📄 Enter path to medical report file: ").strip()
    question = input("❓ Enter your medical question: ").strip()

    if not os.path.exists(file_path):
        print("❌ File not found")
        return

    print("📄 Extracting text...")
    report_text = truncate_text(extract_text_any_file(file_path))

    if not report_text.strip():
        print("❌ No readable text found in file")
        return

    prompt = f"""
You are a medical AI assistant.
This is NOT a medical diagnosis.

Medical Report:
{report_text}

Question:
{question}

Answer briefly and clearly.
""".strip()

    print("🧠 Generating answer...\n")

    answer = generate_response(
        tokenizer,
        model,
        prompt,
        max_new_tokens=MAX_NEW_TOKENS,
    )

    print("✅ ANSWER:\n")
    print(answer)


if __name__ == "__main__":
    main()