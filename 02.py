# Escreva um programa em Python que pergunte três informações ao usuário:
# - É estudante? (uma string: "sim" ou "nao")
# - Dia da semana? (uma string: "terça" ou "outro")
# - Tipo de sala? (uma string:"vip"ou "comum")
#
# O programa deve exibir "Desconto Aplicado!" ou "Valor Integral"
#
# Regra
# O cliente ganha o desconto se for estudante ou for terça e a sala for comum.

estudante = str(input("Você é estudante? "))
dia = str(input("Qual o dia da semana? "))
sala = str(input("Qual o tipo de sala? "))

if estudante == "Sim" or "sim" or dia == "Terça" or "terça":
    if sala == "Comum" or "comum":
        print ("Desconto Aplicado!")
else:
    print ("Valor Integral")
    
   