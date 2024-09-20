nome=input("Digite seu nome:")
idade=int(input("Digite sua idade:"))
print("Seja bem-vindo!",nome,"Por favor preencha as informacoes abaixo para obter sua media!",nome)
nota1=float(input("Digite sua nota em Portugues:"))
nota2=float(input("Digite sua nota em Matematica:"))
faltas=int(input("Quantidade de faltas:"))
print("Sua nota em Portugues:",nota1)
print("Sua nota em Matematica:",nota2)
print("Quantidades de faltas:",faltas)
media=(nota1+nota2)/2
print("Sua media e",media)
if (media>=7 and faltas<=3):
    print("Voce esta aprovado",nome)
else:
    print("Voce esta reprovado",nome)