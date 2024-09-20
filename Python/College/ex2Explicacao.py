#Exercicio 2
senha = input("Senha 8 digitos:")
if(len(senha)==8 and senha.isalnum and not senha.isdigit() and not senha.isalpha()):
    print("Senha Valida")
else:
    print("Senha Invalida")
    
    #Análise da lógica:

#len(senha) == 8:
#Verifica se a senha tem exatamente 8 caracteres. Se a senha tiver mais ou menos de 8 caracteres, a senha será considerada inválida.

#senha.isalnum():
#O método isalnum() retorna True se a senha contém apenas letras e números (sem espaços ou símbolos especiais). Isso garante que a senha seja composta apenas por caracteres alfanuméricos (letras e números).

#not senha.isdigit():
#senha.isdigit() retorna True se a senha contiver apenas números. Ao usar not, estamos verificando se não é composta só de números. Isso é importante porque, para a senha ser válida, ela precisa ter uma combinação de letras e números.

#not senha.isalpha():
#senha.isalpha() retorna True se a senha contiver apenas letras. Com not, garantimos que a senha não seja apenas composta por letras, pois também precisa ter números para ser válida.

#Resumindo a lógica:

#A senha deve ter exatamente 8 caracteres.
#Ela deve conter apenas letras e números (nenhum símbolo especial ou espaço).
#Ela não pode ser apenas números (ou seja, deve ter pelo menos uma letra).
#Ela não pode ser apenas letras (ou seja, deve ter pelo menos um número).
#Quando todas essas condições são atendidas, a senha é válida!