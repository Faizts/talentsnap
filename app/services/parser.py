import pdfplumber
from io import BytesIO
from pdfplumber.utils.exceptions import PdfminerException

def parse_resume(file_content: bytes) -> str:
    try:
        with pdfplumber.open(BytesIO(file_content)) as pdf:
            text = ''
            for page in pdf.pages:
                text += page.extract_text() or ''
            return text.strip()
    except PdfminerException as e:
        raise ValueError("Uploaded file is not a valid PDF or is corrupted.") from e
    except Exception as e:
        raise ValueError("An unexpected error occurred while processing the PDF.") from e
