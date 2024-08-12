from initialization import init , findSimilarPdf 
import os
import time
 
if __name__ == "__main__":

    start = time.time()
    init() 
    end = time.time()
    perfs = end-start

    print(f"Time taken : {perfs:.2f} seconds\n")


    while True:
        try:
            pdf_path = input("Enter the path of the pdf file to be compared: ")

            if not os.path.exists(pdf_path):
                print(f"File {pdf_path} not found")
                continue
            
            start = time.time()
            similar_pdf, similarity = findSimilarPdf(pdf_path)
            end = time.time()

            if similar_pdf:
                perfs = end-start

                print(f"\nMost similar pdf : {similar_pdf['path']}")
                print(f"Similarity percentage : {similarity}%")
                print(f"Time taken : {perfs:.2f} seconds\n")
            else:
                print("No similar pdf found.")
        except Exception as e:
            print(f"Error: {e}")
            continue
        except KeyboardInterrupt as e:
            print("\nExiting...")
            break



