'''O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos trabalhos dos alunos. 
Faça um programa que leia o nome dos 4 alunos e mostre a ordem sorteada.'''

from random import shuffle

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

lista = [n1, n2, n3, n4]

shuffle(lista) #embaralhar a lista

print('A ordem de apresentação será {}'.format(lista))