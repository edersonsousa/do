import fitz  # PyMuPDF

def mapear_areas_pdf(pdf_file):
    doc = fitz.open(pdf_file)
    paginas = []
    for pagina_num in range(len(doc)):
        pagina = doc.load_page(pagina_num)
        colunas_por_pagina = []
        for coluna_num in range(4):  # Lendo 4 colunas por página
            coluna = []
            coluna_x0 = pagina.rect.width / 4 * coluna_num
            coluna_x1 = pagina.rect.width / 4 * (coluna_num + 1)
            for bloco in pagina.get_text("dict")["blocks"]:
                if "lines" in bloco:
                    for linha in bloco["lines"]:
                        linha_x_medio = (linha["bbox"][0] + linha["bbox"][2]) / 2
                        if coluna_x0 <= linha_x_medio <= coluna_x1:
                            texto = ""
                            for span in linha["spans"]:
                                texto += span["text"]
                            coluna.append({"texto": texto, "bbox": fitz.Rect(linha["bbox"])})
            colunas_por_pagina.append(coluna)
        paginas.append(colunas_por_pagina)
    doc.close()
    return paginas



