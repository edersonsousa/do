
import fitz  # PyMuPDF

def mapear_areas_pdf(pdf_file):
    doc = fitz.open(pdf_file)
    paginas = []
    for pagina_num in range(len(doc)):
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


