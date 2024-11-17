""" Faça um algoritmo que leia o salário de um funcionário e mostre seu novo 
salário com 15% de aumento"""

wage = int(input("Digite o salário do funcionário"))

discount = (wage * 15) / 100

new_wage = wage + discount

print("o salário com o aumento ficou: ", new_wage)
