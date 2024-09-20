#Vitor Augusto Rodrigues de Campos
#Exercicio 2
senha = input("Senha 8 digitos:")
if(len(senha)==8 and senha.isalnum and not senha.isdigit() and not senha.isalpha()):
    print("Senha Valida")
else:
    print("Senha Invalida")