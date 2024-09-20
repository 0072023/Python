#Isdigit 🡪 verifica se string possui só números
print('abc123'.isdigit())  #false because own words

print('123456'.isdigit()) #True because own only numbers


texto = input("Digite seu texto para ver se e true ou falso:")
if(texto.isdigit()==True):
    print("Seu texto contem somente numeros entao e verdade:",texto)
else:
    print("Seu texto contem letra e numeros entao e falso:",texto)