#escreva um programa que leia um número inteiro e mostre na tela a sua tabuada.

numero = int(input('digite um número: '))
i = 1
print('\ntabuada de {}'.format(numero))
print('-'*12)

while (i <= 10):
    print('{} x {:2} = {:2}'.format(numero, i, (numero * i)))
    i+=1

print('-'*12)