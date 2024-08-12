import fitz
from PIL import Image
from utils import preprocess_image

def convertPdfToImg(pdf_path):
    doc = fitz.open(pdf_path)
    images = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        img = preprocess_image(img)

        images.append(img)
    return images
