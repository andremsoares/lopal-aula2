# Escreva um programa em Python que peça as seguintes informações:
# - Idade (um número inteiro)
# - Altura em centímetros (um numero inteiro)
# - Tem autorização dos pais? (uma string: "sim" ou "não)
#
# O programa deve exibir "Acesso Liberado!" se o visitante puder andar no brinquedo, ou "Acesso Negado." caso contrário.
#
# Regra
# O visitante pode entrar se:
# - Tiver idade maior ou igual a 12 e altura maior ou igual a 140 ou se tiver autorização igual a "Sim".

idade = int(input("Qual a idade do seu filho? "))
altura = int(input("Qual a altura dele em centímetros? "))
autorizacao = input("Tem autorização dos pais? Responda somente com 'Sim'ou 'Não'")
                    
if idade >= 12 and altura >= 140 or autorizacao == "Sim" or autorizacao == "sim":
    print (f"Acesso Liberado!")
else:
    print (f"Acesso Negado.")
