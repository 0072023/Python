import math
unidade=input("Unidade de medida:")
raio=float(input("Digite o raio para obter a circunferencia do circulo:"))

circunferencia=(2*math.pi)*raio
print("A circuferencia e:",circunferencia)
print("\nA circuferencia e:{:.3f}{}".format(circunferencia,unidade))

