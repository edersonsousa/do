from datetime import date
import io
import re
from tika import parser
from urllib.request import Request, urlopen
from PyPDF2 import PdfReader
from tool_box import pagina

data_atual = date.today().day
print(data_atual)
url = "https://www.imprensaoficial.com.br/downloads/pdf/edicao/20240131EXEC1.pdf"
# pdf = './20240130EXEC1.pdf'
buffer = io.BytesIO(urlopen(Request(url)).read())
reader = PdfReader(buffer)

page = reader.pages[1]
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
    print(f"A sessão SAÚDE vai da página {resultado} até a página {resultadofinal}")
else:
    print("Não encontrei.")
print("O DO hoje possui ......", len(reader.pages), " Páginas")
resultado = resultado - 1
pag_saude = reader.pages[resultado]
texto_saude = pag_saude.extract_text()


resolucao = 0
while resultado <= resultadofinal:
    # print(resultado)
    # print(resultadofinal)
    # reader = PdfReader(pdf)
    pag_saude = reader.pages[resultado]
    texto_saude = pag_saude.extract_text()
    # Usando expressão regular para encontrar os trechos desejados
    # padrao = r'Resolução SS n.*? Esta resolução entra em vigor'
    # padrao = r'Resolução SS n.*? vigor na data'
    padrao = r"Resolução SS.*? IDH"
    padrao_portaria = r"PORTARIA.*? ARTIGO"

    trechos_portaria = re.findall(padrao_portaria, texto_saude, re.DOTALL)
    trechos_resolucao = re.findall(padrao, texto_saude, re.DOTALL)
    # Exibindo os trechos encontrados
    for trecho in trechos_resolucao:
        print(160 * "_")
        print(trecho)
        resolucao += 1
        print(160 * "_")

    resultado = resultado - 1
    for trecho in trechos_portaria:
        print(160 * "_")
        print(trecho)
        resolucao += 1
        print(160 * "_")
# print(resolucao)
# print(len(trecho))
if resolucao > 1:
    print("Encontrei ", resolucao, " Resoluções!")
elif resolucao == 1:
    print("Encontrei ", resolucao, " Resolução!")
else:
    print("Não encontrei nenhuma resolução hoje...")

print("teste.....")
qtd_portaria = 0
while resultado <= resultadofinal:
    pag_saude = reader.pages[resultado]
    print(pag_saude)
    texto_saude = pag_saude.extract_text()
    # Usando expressão regular para encontrar os trechos desejados
    padrao_portaria = r"PORTARIA.*? ARTIGO"
    trechos = re.findall(padrao_portaria, texto_saude, re.DOTALL)
    # Exibindo os trechos encontrados
    for trecho in trechos:
        print(160 * "*")
        print(trecho)
        qtd_portaria += 1
        print(160 * "*")

    resultado = resultado + 1
# print(resolucao)
# print(len(trecho))
if qtd_portaria > 1:
    print("Encontrei ", qtd_portaria, " Portarias!")
elif resolucao == 1:
    print("Encontrei ", qtd_portaria, " Portaria!")
else:
    print("Não encontrei nenhuma portaria hoje...")


print("teste.....")


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
