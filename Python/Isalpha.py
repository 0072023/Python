#Isalpha🡪 verifica se todos os caracteres da string são letras do alfabeto (não inclui números nem espaços).
#True if there are only words
#False if there are numbers or space
string1 = "Python"

string2 = "Python123"

string3 = "Python é legal"

print(string1.isalpha()) # Retorna True, todos os caracteres são letras

print(string2.isalpha()) # Retorna False, contém números

print(string3.isalpha()) # Retorna False, contém espaços