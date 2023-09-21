#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira.

import math
#ou from math import trunc trunc(numero)

numero = float(input('Digite um valor: '))
print('o valor digitado foi {} e a sua porção inteira é {}'.format(numero, math.trunc(numero)))

#print('o valor digitado foi {} e a sua porção inteira é {}'.format(numero, int(numero)))