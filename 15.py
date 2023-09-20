#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado. 

km = float(input('Digite a quantidade de KM percorridos: '))
dias = int(input('Digite a quantidade de dia pelo qual ele foi alugado: '))

precoTotal = (0.15  * km) + (60* dias)

print('O preço a pagar é de {:.2f}R$'.format(precoTotal))