from urllib.request import Request, urlopen
import fitz  # PyMuPDF
from datetime import datetime
from PyPDF2 import PdfReader
import requests
import pdfplumber
import io
#######################################################
#from io import BytesIO

#######################################################

hoje = datetime.now()
global url_cad01
url_cad01 = (
            f"https://www.imprensaoficial.com.br/downloads/pdf/edicao/{hoje:%Y%m%d}EXEC1.pdf"
        )
global url_cad02
url_cad02 = (
            f"https://www.imprensaoficial.com.br/downloads/pdf/edicao/{hoje:%Y%m%d}EXEC2.pdf"
        )
global url_cad03
url_cad03 = (
            f"https://www.imprensaoficial.com.br/downloads/pdf/edicao/{hoje:%Y%m%d}EXEC3.pdf"
        )

def pagina(string):
    numero_atual = ""
    encontrou_numero = False

    for char in string:
        if char.isdigit() or (encontrou_numero and char == "-"):
# Adiciona os dígitos ao número atual
            numero_atual += char
            encontrou_numero = True
        elif encontrou_numero:
# Se já encontrou um número e o próximo caractere não é um dígito, para o loop
            break

# Retorna o próximo número inteiro
    return int(numero_atual) if numero_atual else None
def indice():
##################################Construindo a url do dia###################################
    
################ Carregando o Índice Caderno 01 ################################################
    buffer_cad01 = io.BytesIO(urlopen(Request(url_cad01)).read())
    reader_cad01 = PdfReader(buffer_cad01)
    page_cad01 = reader_cad01.pages[1]
    text_cad01 = page_cad01.extract_text()
################################################################################################
##################Localizando onde está a "Saúde" no sumário do carderno 1 #####################
    resultado = pagina(text_cad01.split("SAÚDE ......")[1])
    ######################Localizando onde acaba a "Saúde" no sumário###############################
    if "POLÍTICAS PARA A MULHER ....." in text_cad01:
            resultadofinal = pagina(text_cad01.split("POLÍTICAS PARA A MULHER .....")[1])
    elif "CULTURA, ECONOMIA E INDÚSTRIA CRIATIVAS ...................." in text_cad01:
            resultadofinal = pagina(
                text_cad01.split("CULTURA, ECONOMIA E INDÚSTRIA CRIATIVAS")[1]
            )
    elif "DESENVOLVIMENTO ECONÔMICO ..." in text_cad01:
            resultadofinal = pagina(text_cad01.split("DESENVOLVIMENTO ECONÔMICO ...")[1])
    elif "MEIO AMBIENTE, INFRAESTRUTURA E LOGÍSTICA ..........." in text_cad01:
            resultadofinal = pagina(
                text_cad01.split("MEIO AMBIENTE, INFRAESTRUTURA E LOGÍSTICA ..........")[1]
            )
    if (resultado and resultadofinal) is not None:
        cad01_total = len(reader_cad01.pages)
        cad01_inicio_saude = resultado
        cad01_fim_saude = resultadofinal
        
############################ Achando CRH no Índice no Caderno 01 ############################################
    try:                   
            cad01_inicio_crh = pagina(text_cad01.split("COORDENADORIA DE RECURSOS HUMANOS")[1])
            if "COORDENADORIA DE CONTROLE DE DOENÇAS ........." in text_cad01:
                cad01_fim_crh = pagina(text_cad01.split("COORDENADORIA DE CONTROLE DE DOENÇAS .........")[1])
            elif "CULTURA, ECONOMIA E INDÚSTRIA CRIATIVAS .................." in text_cad02:
                cad01_fim_crh = pagina(text_cad01.split("CULTURA, ECONOMIA E INDÚSTRIA CRIATIVAS ......")[1])
    except IndexError: 
            cad01_inicio_crh = None
            cad01_fim_crh = None
##################Localizando onde acaba a CRH no sumário ############################################
###################### Carregando o Índice Caderno 02 ################################################
    buffer_cad02 = io.BytesIO(urlopen(Request(url_cad02)).read())
    reader_cad02 = PdfReader(buffer_cad02)
    atos_cad02 = reader_cad02.pages[0]
    page_cad02 = reader_cad02.pages[1]
    text_atos_cad02 = atos_cad02.extract_text()
    text_cad02 = page_cad02.extract_text()
##################Localizando onde está a "Saúde" no sumário do carderno 2 ##################
    resultado_cad02 = pagina(text_cad02.split("SAÚDE ................................................................................................")[1])
######################Localizando onde acaba a "Saúde" no sumário############################
    if "POLÍTICAS PARA A MULHER ....." in text_cad02:
        resultadofinal_cad02 = pagina(text_cad02.split("POLÍTICAS PARA A MULHER .....")[1])
    elif "CULTURA, ECONOMIA E INDÚSTRIA CRIATIVAS ...................." in text_cad02:
        resultadofinal_cad02 = pagina(text_cad02.split("CULTURA, ECONOMIA E INDÚSTRIA CRIATIVAS")[1])
    elif "DESENVOLVIMENTO ECONÔMICO ..." in text_cad02:
        resultadofinal_cad02 = pagina(text_cad02.split("DESENVOLVIMENTO ECONÔMICO ...")[1])
    elif "MEIO AMBIENTE, INFRAESTRUTURA E LOGÍSTICA  ..........." in text_cad02:
        resultadofinal_cad02 = pagina(
            text_cad02.split("MEIO AMBIENTE, INFRAESTRUTURA E LOGÍSTICA  ..........")[1])
    elif "ESPORTES ........................................" in text_cad02:
        resultadofinal_cad02 = pagina(
            text_cad02.split("ESPORTES ..........")[1])
    else:
        resultadofinal_cad02 = None
        
    if (resultado_cad02 and resultadofinal_cad02) is not None:
        cad02_total = len(reader_cad02.pages)
        cad02_inicio_saude = resultado_cad02
        cad02_fim_saude = resultadofinal_cad02
############################ Achando CRH no Índice no Caderno 02 ############################################
    try:                   
            cad02_inicio_crh = pagina(text_cad02.split("COORDENADORIA DE RECURSOS HUMANOS")[1])
            if "COORDENADORIA DE CONTROLE DE DOENÇAS ........." in text_cad02:
                cad02_fim_crh = pagina(text_cad02.split("COORDENADORIA DE CONTROLE DE DOENÇAS .........")[1])
            elif "CULTURA, ECONOMIA E INDÚSTRIA CRIATIVAS .................." in text_cad02:
                cad02_fim_crh = pagina(text_cad02.split("CULTURA, ECONOMIA E INDÚSTRIA CRIATIVAS ......")[1])
    except IndexError: 
            cad02_inicio_crh = None
            cad02_fim_crh = None
######################Localizando onde acaba a CRH no sumário#########################################
    indice = {
            "cad01_total": cad01_total,
            "cad01_inicio_saude": cad01_inicio_saude, 
            "cad01_fim_saude": cad01_fim_saude,
            "cad01_inicio_crh": cad01_inicio_crh,
            "cad01_fim_crh": cad01_fim_crh,
            "cad02_total": cad02_total,
            "cad02_inicio_saude": cad02_inicio_saude,
            "cad02_fim_saude": cad02_fim_saude,
            "cad02_inicio_crh": cad02_inicio_crh,
            "cad02_fim_crh": cad02_fim_crh
            }
    return indice

def resumo_indice():
    
    print(f"Temos um total de {indice()['cad01_total']} páginas no caderno de atos normativos.") if (indice()['cad01_total']) else print(".")
    print(f"Onde a Secretaria da Saúde se encontra da página {indice()['cad01_inicio_saude']} até a página {indice()['cad01_fim_saude']}.")
    print(f"A Coordenadoria de Recursos Humanos se encontra da página {indice()['cad01_inicio_crh']} até a página {indice()['cad01_fim_crh']} do Caderno de Atos Normativos.") if (str(indice()['cad01_inicio_crh'])).isdigit() else print("Não encontrei a CRH no Caderno de Atos Normativos Hoje.")
    print(f"Temos um total de {indice()['cad02_total']} páginas no caderno de atos de pessoal.") if (indice()['cad02_total']) else print(".")
    print(f"Onde a Secretaria da Saúde se encontra da página {indice()['cad02_inicio_saude']} até a página {indice()['cad02_fim_saude']}.")
    print(f"A Coordenadoria de Recursos Humanos se encontra da página {indice()['cad02_inicio_crh']} até a página {indice()['cad02_fim_crh']} do caderno de atos de pessoal.") if (str(indice()['cad02_inicio_crh'])).isdigit() else print("Não encontrei a CRH no Caderno de atos de pessoal Hoje.")
    
###############################

def mapear_areas_pdf(pdf_content, start_page=0, end_page=None):
    doc = fitz.open("pdf", pdf_content)
    if end_page is None:
        end_page = len(doc)
    paginas = []
    for pagina_num in range(start_page, end_page):
        pagina = doc.load_page(pagina_num)
        colunas_por_pagina = []  # Lista para armazenar as áreas de cada coluna na página atual
        for coluna_num in range(4):  # Iterar sobre as 4 colunas
            coluna_x0 = 39.7 + 181.5 * coluna_num
            coluna_x1 = 210 + 181.7 * coluna_num
            coluna_bbox = fitz.Rect(coluna_x0, 52, coluna_x1, 1172.5)  # Bounding box para a coluna atual
            coluna_texto = []  # Lista para armazenar o texto da coluna atual
            for bloco in pagina.get_text("dict")["blocks"]:
                if "lines" in bloco:
                    for linha in bloco["lines"]:
                        linha_x_medio = (linha["bbox"][0] + linha["bbox"][2]) / 2
                        if coluna_x0 <= linha_x_medio <= coluna_x1:
                            for span in linha["spans"]:
                                coluna_texto.append(span["text"])
            colunas_por_pagina.append({"texto": " ".join(coluna_texto), "bbox": coluna_bbox})
        paginas.append(colunas_por_pagina)
    doc.close()
    return paginas

def download_pdf_from_url(url):
    response = requests.get(url)
    return bytes(response.content)


# Especificar a URL e o intervalo de páginas desejado
