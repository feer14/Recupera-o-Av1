5)  Faça um algoritmo que solicite o ano que o usuário nasceu, depois disso, faça o programa descrever se o usuário fará ou já fez 18 anos neste ano.

# Solicita o ano de nascimento ao usuário
ano_nascimento = int(input("Digite o ano em que você nasceu: "))

# Obtém o ano atual
from datetime import datetime
ano_atual = datetime.now().year

# Calcula a idade do usuário
idade = ano_atual - ano_nascimento

# Verifica se o usuário já fez ou fará 18 anos neste ano
if idade == 18:
    print("Você está completando 18 anos neste ano.")
elif idade > 18:
    print("Você já fez 18 anos.")
else:
    print("Você ainda não tem 18 anos.")