3) Faça um algoritmo que solicite um número ao usuário, depois disso, escreva True no console, caso o número tenha dois dígitos (Esteja entre 10 e 99), caso contrário escreva False

# Solicita um número ao usuário 
numero = int(input("Digite um número: ")) 

# Verifica se o número tem dois dígitos (entre 10 e 99) 
dois_digitos = 10 <= numero <= 99 

# Escreve True ou False no console 
print(dois_digitos)
