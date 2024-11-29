import PyPDF2

def read_pdf(pdf_file_path):
    """
    Reads and extracts text from each page of a PDF file.

    Parameters:
    - pdf_file_path (str): The full path to the PDF file to read.

    Returns:
    list: A list where each element is a string containing the text of a page.
    """
    
    # Load PDF file into the program
    try:
        with open(pdf_file_path, "rb") as pdf_import:
            pdf = PyPDF2.PdfReader(pdf_import)
            page_storage = []
            
            # Parse through all pages and store text as strings in a list
            for page in range(len(pdf.pages)):
                page_storage.append(pdf.pages[page].extract_text())

        return page_storage
    
    except FileNotFoundError:
        print(f"Error: The file '{pdf_file_path}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []