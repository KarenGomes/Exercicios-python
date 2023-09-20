#Escreva um programa que converta uma temperatura digitada em °C e converta para °F

C = float(input('Informe a temperatura em °C: '))
F = ((9*C)/5) + 32
print('A temperatura correspondente em °F é de {:.1f}'.format(F))
