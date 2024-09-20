#Isalnum 🡪 verifica se string é alfanumérica (só possui letras e números)
print('abc123'.isalnum())
print('123'.isalnum())
print('#1212'.isalnum())#false because own caracter

teste = input("Faca o teste:")
if(teste.isalnum()==True):
    print("Contem numeros ou letras")
else:
    print("Contem caracteres")