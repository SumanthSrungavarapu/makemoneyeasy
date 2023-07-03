#This code aims to extract data from a pdf
# resources referred:
#https://medium.com/analytics-vidhya/python-packages-for-pdf-data-extraction-d14ec30f0ad0
#Considered packages(these maintain the structure, hopefully some maintain table structure too)
# PDFtotext,PDFminer,Tabula

#using Tabula
import tabula as tabula
path="statement.pdf"
df = tabula.read_pdf(path, pages='all')
print(df[0])