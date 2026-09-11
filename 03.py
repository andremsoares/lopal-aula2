# Escreva um programa em Python que receba as seguintes quatro informações do usuário:
# - Renda Mensal (um número float)
# - Score de Crédito (um número inteiro de 0 a 1000)
# - Possui bens como garantia? (uma string "sim"ou "não")
# - Tem histórico de Inadimplência? (uma string 'sim"ou "não")
#
# O empréstimo será APROVADO se o cliente cumprir uma das duas regras abaixo:
# Regra 1:  Ter renda mensal maior ou igual a R$ 3.000,00 E score de crédito maior ou igual a 600 E NÃO ter histórico de inaimplência.
# Regra 2: Independentemente da renda ou score, se o cliente NÃO tiver histórico de inadimplência E possuir bens como garantia, ele também é aprovado.
#
# Se o cliente não se encaixar em nenhuma das duas regras o empréstimo será REPROVADO.

renda = float(input("Qual sua renda mensal? "))
score = int(input("Qual seu score de crédito? "))
garantia = str(input("Possui bens como garantia? "))
historico = str(input("Tem histórico de inadimplência? "))

if renda >= 3000 and score >= 600 and historico == "não":
    print ("APROVADO")
elif historico == "não" and garantia == "sim":
    print ("APROVADO")
else:
    print ("REPROVADO")
    