# Document representation method:

> 1. I represent the document as by extracting its text with its position in the document.
> 2. I also extract the total number of pages , Images used in the document.
> 3. I also extract the tables and its structure in the document.

# Similarity metrices used in the project:

> I have decided used four metrices to calculate the similarity score between the documents.
>
> 1. I compare the text of the pdf document using the cosine similarity.
> 2. I compare the structure similarity of the pdf by image processing of the pdfs.
> 3. I compare structure using tables columns.
> 4. I compare the logos and other types of images used in the pdf.

# Instructions on how to run:

## Installation:

1. Clone the repository.

   ```bash
   git clone <repository link>
   ```

2. Setup the virtual enviroment .

   > windows :

   ```bash
     python -m venv venv
     venv\Scripts\activate
   ```

   > Linux:

   ```bash
     python3 -m venv venv
     source venv/bin/activate
   ```

   > macOS:

   ```bash
     python3 -m venv venv
     source venv/bin/activate
   ```

3. Install the required packages.

   ```bash
     pip install -r requirements.txt
   ```

4. Create a folder named init_invoices at the root of the project

5. Add the pdfs to the folder(init_invoices) on which you want the system to compare the incoming pdfs

6. On starting up the system will analyze all the pdfs inside the init_invoices

## Running the project:

## Using cli:

```bash
    python3 main.py
```

> output:

```bash
    Enter the path of the pdf file to be compared: <path of the pdf file>
```

> This will return the similarity path to the most similar pdf with its respective similarity score.

```bash
    Most similar pdf : <path to pdf>
    Similarity percentage : <percentage similar>
```

# Dependencies used:

> scikit-learn for TfidfVectorizer and cosine_similarity

> opencv-python for OpenCV functions

> scikit-image for structural_similarity

> Pillow for handling images

> PyMuPDF for working with PDF files

> numpy for numerical operations
