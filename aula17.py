""" Faça um programa que leia o comprimento do cateto oposto e do cateto
 adjacente de um triangulo retangulo, calcule e mostre o comprimmento da 
 hipotenusa"""

import math

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)

print("O comprimento da hipotenusa é:" ,hipotenusa)
