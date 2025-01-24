import requests
import PyPDF2
import io

def read_pdf_from_url(url):
    """
    Downloads a PDF from a URL and extracts its text content.

    Args:
        url (str): The URL of the PDF.

    Returns:
        str: Extracted text from the PDF.
    """
    response = requests.get(url)
    if response.status_code == 200:
        pdf_file = io.BytesIO(response.content)
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
        return text
    else:
        print(f"Failed to fetch PDF from {url}")
        return None
