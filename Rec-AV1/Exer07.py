7) Faça um programa que solicite ao usuário 2 valores, utilize uma condição ternária para escrever qual o maior valor: o primeiro ou o segundo (caso os valores sejam iguais, considere o segundo).

#Solicita dois valores ao usuário
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

# Usa uma condição ternária para determinar o maior valor
maior_valor = valor2 if valor1 <= valor2 else valor1

#Exibe o maior valor
print("O maior valor é:", maior_valor)