# importing required modules
from PyPDF2 import PdfReader
from tool_box import pagina

# creating a pdf reader object
reader = PdfReader("./20231222EXEC1.pdf")
# printing number of pages in pdf file
# print(len(reader.pages))
# getting a specific page from the pdf file
page = reader.pages[1]
# extracting text from page
text = page.extract_text()
# print(text)
# Exemplo de uso
minha_string = text
# print(text)
saude = text.split("SAÚDE ...")
# print(saude[1])
saude_fim = text.split("CULTURA, ECONOMIA E INDÚSTRIA CRIATIVAS ....................")
# print(saude_fim[1])
minha_string = saude[1]
resultado = pagina(minha_string)
resultadofinal = pagina(text.split("CULTURA, ECONOMIA E INDÚSTRIA CRIATIVAS")[1])
print(resultadofinal)
if resultado is not None:
    print(
        "SAÚDE...................................................................................",
        resultado,
    )
else:
    print("Não encontrei.")
# print(saude)
print(len(reader.pages))
resultado = resultado - 1
pag_saude = reader.pages[resultado]
text_saude = pag_saude.extract_text()
# print(text_saude)
# resolucao = text_saude.split('Resolução SS', 1)
# print('_'*160)
# print('Resolução SS', resolucao[1][:800])
# print('_'*160)
import re

# print(type(text_saude))
# Sua string de entrada
texto = "Resolução SS 123: Algum texto a aqui. Resolução SS 456: Outro texto. Esta Resolução entra em vigor na data de sua publicação. Resolução SS 789: Mais um texto. Esta Resolução entra em vigor na data de sua publicação."
# texto = text_saude
# Usando expressão regular para encontrar os trechos desejados
# padrao = r'Resolução .*?Esta Resolução entra em vigor na data de sua publicação'
padrao = r"Resolução SS.*?Esta Resolução entra em vigor na data de sua publicação"

# padrao_saude = r'.*?Resolução *? Esta Resolução entra em vigor na data de sua publicação*?'
padrao_saude = r"Resolução SS.*?Esta Resolução entra em vigor na data de sua"

trechos = re.findall(padrao, texto, re.DOTALL)

trechos_saude = re.findall(padrao_saude, text_saude, re.DOTALL)
# Exibindo os trechos encontrados
# for trecho in trechos:
#    print(trecho)
# print(trechos)
# print(trechos_saude)
# type(trechos_saude)
for trecho_saude in trechos_saude:
    print(trecho_saude, "????????.")
    # type(trecho_saude)
# print(text_saude)
