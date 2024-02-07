from datetime import datetime
import io, re
from tika import parser
from urllib.request import Request, urlopen
from PyPDF2 import PdfReader
from tool_box import pagina

##################################Construindo a url do dia###################################
hoje = datetime.now()
print(f"Data: {hoje:%d/%m/%Y}, Horário: {hoje:%H:%M}")
url_cad01 = (
    f"https://www.imprensaoficial.com.br/downloads/pdf/edicao/{hoje:%Y%m%d}EXEC1.pdf"
)
url_cad02 = (
    f"https://www.imprensaoficial.com.br/downloads/pdf/edicao/{hoje:%Y%m%d}EXEC2.pdf"
)
################ Carregando o Índice Caderno 01 ################################################
buffer_cad01 = io.BytesIO(urlopen(Request(url_cad01)).read())
reader_cad01 = PdfReader(buffer_cad01)
page_cad01 = reader_cad01.pages[1]
text_cad01 = page_cad01.extract_text()
################################################################################################
##################Localizando onde está a "Saúde" no sumário do carderno 1 #####################

resultado = pagina(text_cad01.split("SAÚDE ......")[1])
# print(text_cad01)


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
    print(
        "O Caderno Executivo Atos Normativos hoje possui ",
        len(reader_cad01.pages),
        " Páginas",
    )
    print(
        f"A sessão SAÚDE do Caderno Executivo Atos Normativos vai da página {resultado} até a página {resultadofinal}"
    )
else:
    print("Não encontrei.")
resolucao = 0
portaria = 0
########################################### Percorrendo o D.O.  ############################
while resultado <= resultadofinal:
    pagina_saude = reader_cad01.pages[resultado]
    texto_saude = pagina_saude.extract_text()

    ################################################ Filtrando #################################
    # padrao_resolucao = r'Resolução SS..........*?2024*?..'
    padrao_resolucao = r"Resolução SS n.*?...entra em vigor.*?\."
    # padrao_portaria  = r'PORTARIA....*?2024*?..'
    padrao_portaria = r"\nPortaria.*?.vigor.*?..\.\n"
    trechos_resolucao = re.findall(padrao_resolucao, texto_saude, re.DOTALL)
    trechos_portaria = re.findall(
        padrao_portaria, texto_saude, re.DOTALL | re.IGNORECASE
    )
    # print(trechos_resolucao)
    # print(trechos_portaria)
    resultado += 1
    ########################## Mostrando as resoluções encontradas ###??OK????##################
    for trecho_resolucao in trechos_resolucao:
        # print(100*'_')
        # print(trecho_resolucao)
        # print(100*'_')
        resolucao += 1

    ########################## Mostrando as portarias encontradas ##############################
    for trecho_portaria in trechos_portaria:
        # print(100*'*')
        # print(trecho_portaria)
        # print(100*'*')
        portaria += 1

# print(f'Foram {resolucao} res encontrada(s).')
# print(f'Foram {portaria} portaria encontrada(s).')

#############################################################################################
################ Carregando o Índice Caderno 02 ################################################
buffer_cad02 = io.BytesIO(urlopen(Request(url_cad02)).read())
reader_cad02 = PdfReader(buffer_cad02)
atos_cad02 = reader_cad02.pages[0]
page_cad02 = reader_cad02.pages[1]
text_atos_cad02 = atos_cad02.extract_text()
text_cad02 = page_cad02.extract_text()
################################  Atos do Gavernador  ###########################################

# print(text_atos_cad02)
##Filtrando.....
#print(100 * "_", "\n")
#print("Atos do Governador")
#print(100 * "_", "\n")
padrao_atos_cad02 = r"SECRETARIA DA SAÚDE.*?.Autorizando.*?...\.\n"
trechos_atos_cad02 = re.findall(
    padrao_atos_cad02, text_atos_cad02, re.DOTALL | re.IGNORECASE
)
for trecho_atos_cad02 in trechos_atos_cad02:
    print(100 * "*")
    print(trecho_atos_cad02)
    print(100 * "*")
    # atos_cad02 += 1

#### Mostrando
##################Localizando onde está a "Saúde" no sumário do carderno 2 ##################
resultado_cad02 = pagina(
    text_cad02.split(
        "SAÚDE ................................................................................................"
    )[1]
)
######################Localizando onde acaba a "Saúde" no sumário############################
if "POLÍTICAS PARA A MULHER ....." in text_cad02:
    resultadofinal_cad02 = pagina(text_cad02.split("POLÍTICAS PARA A MULHER .....")[1])
elif "CULTURA, ECONOMIA E INDÚSTRIA CRIATIVAS ...................." in text_cad02:
    resultadofinal_cad02 = pagina(
        text_cad02.split("CULTURA, ECONOMIA E INDÚSTRIA CRIATIVAS")[1]
    )
elif "DESENVOLVIMENTO ECONÔMICO ..." in text_cad02:
    resultadofinal_cad02 = pagina(text_cad02.split("DESENVOLVIMENTO ECONÔMICO ...")[1])
elif "MEIO AMBIENTE, INFRAESTRUTURA E LOGÍSTICA  ..........." in text_cad02:
    resultadofinal_cad02 = pagina(
        text_cad02.split("MEIO AMBIENTE, INFRAESTRUTURA E LOGÍSTICA  ..........")[1]
    )
if (resultado_cad02 and resultadofinal_cad02) is not None:
    print(
        "O Caderno Executivo Atos de Pessoal hoje possui ",
        len(reader_cad02.pages),
        " Páginas",
    )
    print(
        f"A sessão SAÚDE do Caderno Executivo Atos de Pessoal vai da página {resultado_cad02} até a página {resultadofinal_cad02}"
    )
else:
    print("Não encontrei.")

############################ Achando CRH no Índice ####################################
resultado_crh = pagina(text_cad02.split("COORDENADORIA DE RECURSOS HUMANOS")[1])
#############################################################################################
######################Localizando onde acaba a CRH no sumário############################
if "COORDENADORIA DE CONTROLE DE DOENÇAS ........." in text_cad02:
    resultadofinal_crh_cad02 = pagina(
        text_cad02.split("COORDENADORIA DE CONTROLE DE DOENÇAS .........")[1]
    )

print(
    "Coordenadoria de RECURSOS HUMANOS",
    resultado_crh,
    " até ",
    resultadofinal_crh_cad02,
)

####################LENDO#############################LENDO################################

resultado_cad02 = resultado_cad02 - 1
pag_saude_cad02 = reader_cad02.pages[resultado_cad02]
texto_saude_cad02 = pag_saude_cad02.extract_text()
resolucao_cad02 = 0
cessando_cad02 = 0


############################### Percorrendo o D.O. Caderno 02 #############################
while resultado_cad02 <= resultadofinal_cad02:
    pagina_saude_cad02 = reader_cad02.pages[resultado_cad02]
    texto_saude_cad02 = pagina_saude_cad02.extract_text()
    # print(texto_saude_cad02)
    ################################## Filtrando Caderno 02 ###################################
    # padrao_resolucao = r'Resolução SS..........*?2024*?..'
    padrao_resolucao_cad02 = r"Resolução SS.........*?...\.\n"
    trechos_resolucao_cad02 = re.findall(
        padrao_resolucao_cad02, texto_saude_cad02, re.DOTALL | re.IGNORECASE
    )

    # padrao_portaria  = r'PORTARIA....*?2024*?..'
    padrao_cessando_cad02 = (
        r"\nCessando...................................................*?\.\nDESIGNANDO"
    )
    trechos_cessando_cad02 = re.findall(
        padrao_cessando_cad02, texto_saude_cad02, re.DOTALL | re.IGNORECASE
    )
    # print(trechos_resolucao)
    # print(trechos_portaria)
    resultado_cad02 += 1
    ################ Mostrando as resoluções encontradas no caderno 02 ########################
    for trecho_resolucao_cad02 in trechos_resolucao_cad02:
        # print(100*'_')
        # print(trecho_resolucao_cad02)
        #print(100*'_')
        resolucao_cad02 += 1
    ################# Mostrando as portarias encontradas no Caderno 02#########################
    for trecho_cessando_cad02 in trechos_cessando_cad02:
        # print(100*'*')
        # print(trecho_cessando_cad02)
        #print(100*'*')
        cessando_cad02 += 1
# print(concedendo_cad02)
# print(cessando_cad02)
