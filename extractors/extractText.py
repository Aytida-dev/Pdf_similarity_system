import fitz
import re
def extractText(pdf_path):
    try:
        pdf_document = fitz.open(pdf_path)
        text = ""
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            text += page.get_text()

        if text.strip():
            text = text.lower()
            text = re.sub(r'\s+', ' ', text)
            text = re.sub(r'[^a-z0-9\s]', '', text)

        return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return ""