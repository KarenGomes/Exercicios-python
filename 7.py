#Desenvolva um programa que leia duas notas de um aluno, calcule e mostre a sua média: 

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

print('A média entre {} e {} é {:.1f}'.format(nota1, nota2, ((nota1 + nota2)/2)))