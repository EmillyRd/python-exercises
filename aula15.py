"""Escreva umm programa que pergunte a quantidade de km percorridos por um 
carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o 
preço a pagar,  sabendo que o carro custa R$60 por dia e R$0,15 por km rodado."""

amount_traveled = int(input("Qual é a quantidade percorrida? "))
days = int(input("Quantidade de dias que foi alugado: "))

price_day = day * 60
kilometer = amount_traveled * 0.15

total_price = price_day + kilometer

print("O toal a pagar ficou: ", total_price)
