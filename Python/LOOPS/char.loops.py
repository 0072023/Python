texto = input("Digite um texto:")
digitos = 0
for char in texto:
        if char.isdigit():
                digitos += 1
                print("Numeros de digitos:",digitos)