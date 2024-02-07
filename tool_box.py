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
