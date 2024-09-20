nota1=float(input("Digite sua nota em Portugues:"))
nota2=float(input("Digite sua nota em Matematica:"))
media=(nota1+nota2)/2
print("Sua media e",media)
if(media<=7):
    print("reprovado")
else:
    print("aprovado")