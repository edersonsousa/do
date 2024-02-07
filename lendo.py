import io
from urllib.request import Request, urlopen
from PyPDF2 import PdfReader
from csv import reader

url = "https://www.imprensaoficial.com.br/downloads/pdf/edicao/20240131EXEC1.pdf"
"""
        :param url: url to get pdf file
        :return: PdfFileReader object
"""
remote_file = urlopen(Request(url)).read()
memory_file = io.BytesIO(remote_file)
pdf_file = PdfReader(memory_file)

reader = PdfReader(memory_file)
# reader2 = PdfReader(pdf_file)

page = reader.pages[0]
print(page)
