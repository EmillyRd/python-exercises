""" O  mesmo professor do desafio anterior quer sortear a ordem de apresentação
 de trabalho dos alunos. Faça um programa que leia o nome dos quatros alunos
e mostre a ordem sorteada"""

import random

aluno1 = input("Digite o nome do aluno: ")
aluno2 = input("Digite o nome do aluno: ")
aluno3 = input("Digite o nome do aluno: ")
aluno4 = input("Digite o nome do aluno: ")

lista_alunos = ['Amanda','Brenda','Camilo','Debora']

sorteio = random.shuffle(lista_alunos)

for i,aluno in enumerate(lista_alunos,start=1):
  print(f"{i}º: {aluno}")
