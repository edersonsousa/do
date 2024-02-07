# importing required modules
from datetime import date
import re
from tika import parser


from PyPDF2 import PdfReader
from tool_box import pagina

# creating a pdf reader object
# https://www.imprensaoficial.com.br/downloads/pdf/edicao/20240130EXEC1.pdf

# raw = parser.from_file('./20240130EXEC1SAUDE.pdf')
# raw = ['content']

# print(raw)


pdf = "./20240130EXEC1.pdf"
reader = PdfReader(pdf)
# getting a specific page from the pdf file
page = reader.pages[1]
# extracting text from page
text = page.extract_text()

# Localizando onde está a "Saúde" no sumário
resultado = pagina(text.split("SAÚDE ......")[1])
# Localizando onde acaba a "Saúde" no sumário
if "POLÍTICAS PARA A MULHER ....." in text:
    resultadofinal = pagina(text.split("POLÍTICAS PARA A MULHER .....")[1])
elif "CULTURA, ECONOMIA E INDÚSTRIA CRIATIVAS ...................." in text:
    resultadofinal = pagina(text.split("CULTURA, ECONOMIA E INDÚSTRIA CRIATIVAS")[1])
elif "DESENVOLVIMENTO ECONÔMICO ..." in text:
    resultadofinal = pagina(text.split("DESENVOLVIMENTO ECONÔMICO ...")[1])
elif "COORDENADORIA DE SERVIÇOS DE SAÚDE ..........." in text:
    resultadofinal = pagina(
        text.split("COORDENADORIA DE SERVIÇOS DE SAÚDE ..........")[1]
    )

if (resultado and resultadofinal) is not None:
    print(f"O Tópico SAÚDE vai da página {resultado} até a página {resultadofinal}")
else:
    print("Não encontrei.")
print("O Cardeno Executivo Seção 1 hoje possui ......", len(reader.pages), " Páginas")
resultado = resultado - 1
pag_saude = reader.pages[resultado]
texto_saude = pag_saude.extract_text()
# print(texto_saude)
# Usando expressão regular para encontrar os trechos desejados
padrao = r"Resolução SS.*?publicação."
trechos = re.findall(padrao, texto_saude, re.DOTALL)
# Exibindo os trechos encontrados
# for trecho in trechos:
#    print(trecho)
data_atual = date.today().day
print(data_atual)

while resultado <= resultadofinal:
    # print(resultado)
    # print(resultadofinal)
    reader = PdfReader(pdf)
    pag_saude = reader.pages[resultado]
    texto_saude = pag_saude.extract_text()
    # Usando expressão regular para encontrar os trechos desejados
    padrao = r"Resolução SS.*? Esta resolução entra em vigor"
    trechos = re.findall(padrao, texto_saude, re.DOTALL)
    # Exibindo os trechos encontrados
    for trecho in trechos:
        print(trecho)
    resultado = resultado + 1
    # print(trechos)


# texto = "Resolução SS 123: Algum texto a aqui. Resolução SS 456: Outro texto. Esta Resolução entra em vigor na data de sua publicação. Resolução SS 789: Mais um texto. Esta Resolução entra em vigor na data de sua publicação."
# padrao = r'Resolução SS.*?Esta Resolução entra em vigor na data de sua publicação'

# padrao_saude = r'Resolução SS.*?Esta Resolução entra em vigor na data de sua publicação'

# trechos = re.findall(padrao, texto, re.DOTALL)


# print(text_saude)
# print(texto)

# print(text_saude)
# trechos_saude = re.findall(padrao, text_saude, re.DOTALL)
# print(trechos_saude)
# for trecho_saude in trechos_saude:
#    print(trecho_saude, "????????.")
#    type(trecho_saude)
# print(text_saude)
