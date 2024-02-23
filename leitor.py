from datetime import datetime
from tool_box import indice, resumo_indice

resumo_indice()


# Exemplo de uso
colunas_por_pagina = mapear_areas_pdf(pdf_file, start_page, end_page)

for num_pagina, colunas_pagina in enumerate(colunas_por_pagina):
    print(f"Página {num_pagina + 1}:")
    for num_coluna, coluna in enumerate(colunas_pagina):
        print(f"Coluna {num_coluna + 1}:")
        coluna_bbox = coluna["bbox"]
        print("Texto:", str(coluna["texto"]).replace("\n",""))
        print("Bounding Box:", coluna_bbox)
