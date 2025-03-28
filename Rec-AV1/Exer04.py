4) faça um algoritmo que solicite 3 notas para o usuário, calcule a média e indique se o aluno foi aprovado ou reprovado (nota precisar ser maior ou igual à sete para o aluno ser aprovado)

#Solicita as três notas ao usuário
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))

#Calcula a média das notas
media = (nota1 + nota2 + nota3) / 3

#Verifica se o aluno foi aprovado ou reprovado
if media >= 7:
    print("Aprovado! Sua média foi:", round(media, 2))
else:
    print("Reprovado. Sua média foi:", round(media, 2))