""" Um professor quer sortear um dos seus quatros alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome delas e escrevendo o 
nome do escolhido"""

import random

aluno1 = input("Digite o nome do aluno 1: ")
aluno2 = input("Digite o nome do aluno 2: ")
aluno3 = input("Digite o nome do aluno 3: ")
aluno4 = input("Digite o nome do aluno 4: ")

lista_alunos = ['Emilly', 'Maria Cecília', 'Suriane', 'Isabelle']

sorteio = random.choice(lista_alunos)

print("O aluno sorteado é: ", sorteio)