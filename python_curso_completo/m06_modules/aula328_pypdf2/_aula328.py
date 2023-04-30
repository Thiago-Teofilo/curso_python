from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter, PdfMerger

# Parte 1 - PdfReader:

ROOT = Path(__file__).parent
FILES = ROOT / 'pdfs_originais'
NEW_DIR = ROOT / 'arquivos_novos'

PDF_FILE =  FILES / 'R20230414.pdf'
NEW_DIR.mkdir(exist_ok=True)

reader = PdfReader(PDF_FILE)

page0 = reader.pages[0]
image0 = page0.images[0]

# with open(NEW_DIR / 'imagem0.png', 'wb') as  fp:
#     fp.write(image0.data)

# =============================================================

# Parte 2 - PdfWriter

# writer = PdfWriter()

# with open(NEW_DIR / 'page.pdf', 'wb') as fp:
#     for page in reader.pages:
#         writer.add_page(page)
#     writer.write(fp)

# =============================================================

# Parte 3 - PdfMerger


# Separando as páginas do PDF em arquivos diferentes
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(NEW_DIR / f'page{i}.pdf', 'wb') as fp:
        writer.add_page(page)
        writer.write(fp) 

files = [
    NEW_DIR / 'page0.pdf',
    NEW_DIR / 'page1.pdf',
]

merger = PdfMerger()
for file in files:
    merger.append(file)

with open(NEW_DIR / 'Merged.pdf', 'wb') as fp:
    merger.write(fp)