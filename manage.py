from PIL import Image
import pytesseract
import os
import sys
import tqdm
from PyPDF2 import PdfWriter, PdfReader
import io

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\v.ahmedov\AppData\Local\Tesseract-OCR\tesseract.exe"
# path1 = "elements\\wetransfer\\IMG_0096.jpeg"
# path2 = "elements\\wetransfer\\IMG_0125.jpeg"

# img1 = Image.open(path1)
# img2 = Image.open(path2)

in_dir = "elements\\wetransfer\\"
pdf_pages = []
out_dir = "test.pdf"

# C:\Users\v.ahmedov\AppData\Local\Tesseract-OCR

for filename in tqdm.tqdm(os.listdir(in_dir), desc='Process image read:'):
    print(filename)
    img = Image.open(os.path.join(in_dir, filename))
    pdf = pytesseract.image_to_pdf_or_hocr(img, lang='eng', extension='pdf')
    pdf_pages.append(pdf)

pdf_writer = PdfWriter()

for page in pdf_pages:
    pdf = PdfReader(io.BytesIO(page))
    pdf_writer.addPage(pdf.getPage(0))

file = open(out_dir, "w+b")
pdf_writer.write(file)
file.close()

# text1 = pytesseract.image_to_pdf_or_hocr(img1, lang='eng', extension='pdf')
# text2 = pytesseract.image_to_pdf_or_hocr(img2, lang='eng', extension='pdf')

# text = text1 + text2

# print(text1, text2, text, sep='\n--------------')

# with open('test.pdf', 'w+b') as f:
#     f.write(text)  # pdf type is bytes by default
