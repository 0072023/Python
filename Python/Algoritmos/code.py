peso=float(input("Digite seu peso:"))
altura=float(input("Digite sua altura:"))
imc=peso/(altura**altura)
print("Seu imc e",imc)
if(imc<18.5):
    print("imc abaixo do peso")
elif(imc>24.9):
    print("imc acima do peso")
else:
    print("imc normal")