from datetime import datetime
import fitz  # PyMuPDF

from tool_box import indice, resumo_indice, mapear_areas_pdf, download_pdf_from_url

#resumo_indice()


pdf_file = "example.pdf"

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


# Limite da área de cada coluna
limites_colunas = [
    fitz.Rect(39.7, 52, 210, 1172.5),
    fitz.Rect(219.2, 52, 390.9, 1172.5),
    fitz.Rect(398.7, 52, 570.5, 1172.5),
    fitz.Rect(578, 52, 750, 1172.5)
]
url = url_cad01
start_page = 30
end_page = 31

# Baixar o PDF e extrair texto
pdf_content = download_pdf_from_url(url)
colunas_por_pagina = mapear_areas_pdf(pdf_content, start_page, end_page)

for num_pagina, colunas_pagina in enumerate(colunas_por_pagina):
    print(f"Página {start_page + 1}:")
    for num_coluna, coluna in enumerate(colunas_pagina):
        print(f"Coluna {num_coluna + 1}:")
        coluna_bbox = coluna["bbox"]
        print("Começa:", str(coluna["texto"])[:100].replace("\n",""))
        print("Bounding Box:", coluna_bbox)
        print("Termina:", str(coluna["texto"])[-100:].replace("\n",""))
    start_page = start_page + 1
        