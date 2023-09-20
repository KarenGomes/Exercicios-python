#faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento. 

salario = float(input('Digite o salário do funcionário: '))
aumento = salario + (salario * (15/100))

print('O novo salário com o reajuste de 15% é de {:.2f}'.format(aumento))