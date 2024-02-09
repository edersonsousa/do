from tool_box import mapear_areas_pdf
pdf_file = "example.pdf"

# Exemplo de uso
#pdf_file = "example.pdf"
colunas_por_pagina = mapear_areas_pdf(pdf_file)
for num_pagina, colunas_por_pagina in enumerate(colunas_por_pagina):
    print(f"Página {num_pagina + 1}:")
    for num_coluna, coluna in enumerate(colunas_por_pagina):
        print(f"Coluna {num_coluna + 1}:")
        print(colunas_por_pagina)
        for i, area in enumerate(coluna):
            print(f"Área {i + 1}:")
            print("Texto:", area["texto"])
            print("Bounding Box:", area["bbox"])
