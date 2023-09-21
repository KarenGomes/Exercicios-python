'''Faça um programa que leia o comprimento do cateto oposto e adjacente de um triangulo retângulo.
calcule e mostre o comprimento da hipotenusa'''
import math 

catOposto = float(input('Digite o valor do cateto oposto:'))
catAdjacente =  float(input('Digite o valor do cateto adjacente:'))

'''
hipotenusa = (pow(catOposto, 2) + pow(catAdjacente, 2))**(1/2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))'''

hipotenusa = math.hypot(catOposto, catAdjacente)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))