""" Crie um programa que leia um número real qualquer pelo teclado e mostre na 
tela a sua porção inteira"""

import math

number = float(input("Digite um número: "))

portion_floor = math.floor(number)

print("A porção inteira é:", portion_floor)
