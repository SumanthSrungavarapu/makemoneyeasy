#This code aims to extract data from a pdf
# resources referred:
#https://medium.com/analytics-vidhya/python-packages-for-pdf-data-extraction-d14ec30f0ad0
#Considered packages(these maintain the structure, hopefully some maintain table structure too)
# PDFtotext,PDFminer,Tabula

path="statement.pdf"

#using Tabula
import tabula as tabula
import pandas as pd
def tabula_extract():
    df = tabula.read_pdf(path, pages='all')
    df=pd.concat(df)
    print(df)

#Using PDFminer
#what insterested me is It can also convert PDF files into other file formats like HTML/XML
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
def pdfminer_extract(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    # device = TextConverter(rsrcmgr, retstr, codec=codec,laparams=laparams)
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    text = retstr.getvalue()
    fp.close()
    device.close()
    retstr.close()
    return text
pdf_miner_text = pdfminer_extract(path)
# print(pdf_miner_text)

#having hard time to install pdftotext package
#Using PDFtotext
# import pdftotext
# # Load your PDF
# with open(path, "rb") as f:
#     pdf = pdftotext.PDF(f)
# # Read all the text into one string
# pdftotext_text = "\n\n".join(pdf)
# print(pdftotext)