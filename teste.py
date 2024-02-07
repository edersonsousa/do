import pdfplumber
import os

pdf = pdfplumber.open("./20240111EXEC1.pdf")

# Número de páginas
print("Temos hoje :", len(pdf.pages), "páginas no DO")


# Raspando uma
page = pdf.pages[1]
# print(page)

text = page.extract_text()
lista = text.split("SAÚDE")
pagina = print("A Saúde está na página ", lista[1][87:90])

saude = pdf.pages[25]
text_saude = saude.extract_text()
# print(text_saude)


# print(text)
# for l in lista:
#    if "SAÚDE" in l:
#        print(l)
#        pos = lista.index(l)
#        print(pos)

pdf = pdfplumber.open("./20240110EXEC1.pdf")

# Número de páginas
print("Temos hoje :", len(pdf.pages), "páginas no DO")


# Raspando uma
page = pdf.pages[1]
# print(page)

text = page.extract_text()
lista = text.split(" SAÚDE")
pagina = print("A Saúde está na página ", lista[1][86:89])

saude = pdf.pages[25]
text_saude = saude.extract_text()
