import fitz  # PyMuPDF
import requests

# Path to your real PDF
pdf_path = r"C:\Users\ccape\Downloads\12943_2020_Article_1258.pdf"

# Extract text from PDF in smaller chunks
def extract_text_chunks(pdf_path, chunk_size=3000):
    doc = fitz.open(pdf_path)
    text_chunks = []
    current_text = ""

    for page in doc:
        current_text += page.get_text() + "\n"

        if len(current_text) >= chunk_size:
            text_chunks.append(current_text)
            current_text = ""  # Reset current chunk

    if current_text:  # Add any remaining text
        text_chunks.append(current_text)

    return text_chunks

# Process each chunk separately
text_chunks = extract_text_chunks(pdf_path)

# Summarize each chunk and combine results
summary = ""
for i, chunk in enumerate(text_chunks):
    print(f"\nProcessing chunk {i+1}/{len(text_chunks)}...\n")
    
    prompt = f"Summarize this section of a research paper:\n\n{chunk}"
    
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": prompt, "stream": False}
    )
    
    summary += f"\n=== Summary of Section {i+1} ===\n" + response.json()["response"]

# Print the full summary
print("\n=== FINAL SUMMARY ===\n")
print(summary)
