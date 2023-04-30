from PyPDF2 import PdfReader
from pathlib import Path

ROOT = Path(__file__).parent
PDF_DIR = ROOT / 'pdfs_originais'
PDF_FILE = list(PDF_DIR.iterdir())[0]

reader = PdfReader(PDF_FILE)

page_count = len(reader.pages)

print(f'PDF contém um total de {page_count} página(s)!')