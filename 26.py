'''Faça um programa que leia uma frase pelo teclado e mostre: 
- Quantas vezes aparece a letra A
- Em que posição ela aparece pela primeira vez
- Em que posição ela aparece a última vez.'''

frase = input('Digite uma frase: ').lower()

print('A letra A aparece {} vezes na frase'.format(frase.count('a')))
print('A primeira letra aparece na posição {}'.format(frase.find('a')+1))
print('A primeira letra aparece na posição {}'.format(frase.rfind('a')+1))