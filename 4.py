#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

algo = input('digite algo: ') #um objeto.
print('o tipo primitivo desse valor é ', type(algo))
print('Só tem espaços?', algo.isspace())
print('é um número?', algo.isnumeric())
print('é alfabético?', algo.isalpha())
print('é alfanumérico?', algo.isalnum())
print('Está em maiúscula?', algo.isupper())
print('Está em minúscula?', algo.islower())
print('Está capitalizada?', algo.istitle()) #maiúscula e minúscula