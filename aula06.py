"""Crie um algoritmo que leia um numero e mostre seu dobro, triplo
 e raiz quadrada"""

import math

number = int(input("Digite um número: "))

double = number * 2

triple = number * 3

square_root = math.sqrt(number)

print(f"o dobro é: {double}")
print(f"o triplo é: {triple}")
print(f"a raiz quadrada é: {square_root}")
