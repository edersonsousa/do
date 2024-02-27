import fitz  # PyMuPDF
from tool_box import mapear_areas_pdf

#pdf_file = "CRH20240214EXEC2.pdf"
pdf_file = "indicehoje.pdf"

# Limite da área de cada coluna
limites_colunas = [
    fitz.Rect(39.7, 52, 210, 1172.5),
    fitz.Rect(219.2, 52, 390.9, 1172.5),
    fitz.Rect(398.7, 52, 570.5, 1172.5),
    fitz.Rect(578, 52, 750, 1172.5)
]
# Exemplo de uso
colunas_por_pagina = mapear_areas_pdf(pdf_file)

for num_pagina, colunas_pagina in enumerate(colunas_por_pagina):
    print(f"Página {num_pagina + 1}:")
    for num_coluna, coluna in enumerate(colunas_pagina):
        print(f"Coluna {num_coluna + 1}:")
        coluna_bbox = coluna["bbox"]
        # Verificar se a coluna está dentro dos limites
        if limites_colunas[num_coluna].intersects(coluna_bbox):
            print("Texto:", str(coluna["texto"]).replace("\n",""))
            print("Bounding Box:", coluna_bbox)
