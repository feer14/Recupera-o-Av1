 Faça um programa que solicite ao usuário sua idade, depois disso, exiba a classificação etária de acordo com as faixas de valores:

 #Solicita a idade do usuário
idade = int(input("Por favor, digite sua idade: "))

#Determina a classificação etária
if idade < 0:
    print("Idade inválida.")
elif idade <= 12:
    print("Classificação: Criança")
elif idade <= 17:
    print("Classificação: Adolescente")
elif idade <= 59:
    print("Classificação: Adulto")
else:
    print("Classificação: Idoso")