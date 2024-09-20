nota1=float(input("Digite sua nota em Portugues:"))
nota2=float(input("Digite sua nota em Matematica:"))
faltas=int(input("Quantidade de faltas:"))
media=(nota1+nota2)/2
print("Sua media e",media)
if (media>=7 and faltas<=3):
    print("aprovado")
else:
    print("reprovado")