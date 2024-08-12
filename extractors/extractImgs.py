import io
from PIL import Image
import fitz  
from utils import preprocess_image

def extractImg(pdf_path):
    try:
        pdf_document = fitz.open(pdf_path)
        images = []
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            image_list = page.get_images(full=True)
            for img in image_list:
                xref = img[0]
                base_image = pdf_document.extract_image(xref)
                image_bytes = base_image["image"]
                image = Image.open(io.BytesIO(image_bytes))

                image = preprocess_image(image)

                images.append(image)
        return images
    except Exception as e:
        print(f"Error extracting images from PDF: {e}")
        return []
    

