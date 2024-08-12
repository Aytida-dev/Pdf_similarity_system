import os
import multiprocessing
import numpy as np

from extractors.extractText import extractText
from extractors.convertPdfToImg import convertPdfToImg
from extractors.extractColumns import extractColumns
from extractors.extractImgs import extractImg

from similarityFunctions.calculateTextSimilarity import calculateTextSimilarity
from similarityFunctions.calculateImgSimilarity import calculateImgSimilarity
from similarityFunctions.compareTables import compareTables

PDF_MAP = []

def compare_pdf(args):
    new_pdf_data, stored_pdf_data = args

    text_similarity = calculateTextSimilarity(new_pdf_data["text"], stored_pdf_data["text"])
    structure_similarity = calculateImgSimilarity(new_pdf_data["structure"], stored_pdf_data["structure"])
    table_diff = compareTables(new_pdf_data["columns"], stored_pdf_data["columns"])
    img_similarity = calculateImgSimilarity(new_pdf_data["images"], stored_pdf_data["images"])
    
    return (text_similarity + structure_similarity + table_diff + img_similarity) / 4
   
def findSimilarPdf(pdf_path):
    if not os.path.exists(pdf_path):
        print(f"File {pdf_path} not found")
        return None, 0.0

    text = extractText(pdf_path)
    pdf = convertPdfToImg(pdf_path)
    columns = extractColumns(pdf_path)
    images = extractImg(pdf_path)

    new_pdf_data = {
        "text": text,
        "structure": pdf,
        "columns": columns,
        "images": images
    }
    
    with multiprocessing.Pool() as pool:
        similarities = pool.map(compare_pdf, [(new_pdf_data, pdf_data) for pdf_data in PDF_MAP])
    
    max_index = np.argmax(similarities)
    return PDF_MAP[max_index], (similarities[max_index] * 100).round(3)


def process_pdf(filename, init_folder):
    pdf_path = os.path.join(init_folder, filename)
    return {
        "path": pdf_path,
        "text": extractText(pdf_path),
        "structure": convertPdfToImg(pdf_path),
        "columns": extractColumns(pdf_path),
        "images": extractImg(pdf_path)
    }

def init():
    print("Initializing pdf structure...")
    init_folder = "init_invoices"
    if not os.path.exists(init_folder):
        print("init_invoices folder not found...")
        print("init_invoices folder created, please add the pdf files to be compared..")
        os.makedirs(init_folder)
        os._exit(0)

    pdf_files = [f for f in os.listdir(init_folder) if f.lower().endswith(".pdf")]
    
    if not pdf_files:
        print("No pdf files found in init_invoices folder exiting...")
        os._exit(0)

    with multiprocessing.Pool() as pool:
        results = pool.starmap(process_pdf, [(filename, init_folder) for filename in pdf_files])

    global PDF_MAP
    PDF_MAP = results

    print(f"{len(PDF_MAP)} pdf files processed and ready for comparison...")
