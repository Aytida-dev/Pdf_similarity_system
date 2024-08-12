import fitz

def extractColumns(pdf_path):
    columns = []
    pdf_doc = fitz.open(pdf_path)
    for page_num in range(pdf_doc.page_count):
        try:
            page = pdf_doc[page_num]
            tabs = page.find_tables()
            for tab in tabs:
                header = tab.header
                columns.extend(header.names)
        except Exception as e:
            print(f"No tables on page {page_num + 1} of {pdf_path}: {e}")
    pdf_doc.close()
    return set(columns)