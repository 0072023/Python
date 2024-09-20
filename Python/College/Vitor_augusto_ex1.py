# Solicitando uma string ao usuário
texto_usuario = input("Digite um texto: ")
# Inicializando os contadores
letras = 0
digitos = 0
outros = 0
# Percorrendo cada caractere do texto usando o laço for
for char in texto_usuario:
        if char.isalpha():
                letras += 1 # Incrementa o contador de letras
        elif char.isdigit():
                digitos += 1 # Incrementa o contador de dígitos
        else:
                outros += 1 # Incrementa o contador de outros caracteres
# Exibe o resultado
print(letras)
print(digitos)
print(outros)