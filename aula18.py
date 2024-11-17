""" Faça um programa que leia um ângulo qualquer e mostre na tela o valor do
 seno,cosseno e tangente desse ângulo"""

import math

angle = float(input("Digite o valor do ângulo em graus: "))

angle_radians = math.radians(angle)

sen = math.sin(angle_radians)
cos = math.cos(angle_radians)
tan = math.tan(angle_radians)

print("Seno: ", sen)
print("Cosseno: ", cos)
print(f"Tangente: ", tan)
