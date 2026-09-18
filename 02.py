# Escreva um programa em Python que pergunte três informações ao usuário:
# - É estudante? (uma string: "sim" ou "nao")
# - Dia da semana? (uma string: "terça" ou "outro")
# - Tipo de sala? (uma string:"vip"ou "comum")
#
# O programa deve exibir "Desconto Aplicado!" ou "Valor Integral"
#
# Regra
# O cliente ganha o desconto se for estudante ou for terça e a sala for comum.

estudante = input("Você é estudante? ")
dia = input("Qual o dia da semana? ")
sala = input("Qual o tipo de sala? ")

if estudante == "sim" or dia == "terça":
    if sala == "comum":
        print ("Desconto Aplicado!")
else:
    print ("Valor Integral")
    
   