""" Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pinta-lá sabendo 
que cada litro de tinta pinta uma área de 2m2"""

width = int(input("Digite a largura"))
height = int(input("Digite a altura"))

area = width * height

amount_of_ink = area / 2

print("a area: ", area)
print("a quantidade de tinta necessária: ", amount_of_ink)