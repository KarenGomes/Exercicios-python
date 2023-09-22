'''Crie um programa que leia o nome completo de uma pessoa e mostre: 
- o nome com todas as letras maiusculas e minusculas
- quantas letras ao todo (sem condiderar espaços)
- quantas letras tem o primeiro nome'''

nomeCompleto = input('Digite seu nome completo: ').strip() #remove espaços

print('Seu nome com todas as letras maiúsculas: {}'.format(nomeCompleto.upper()))
print('Seu nome com todas as letras minúsculas: {}'.format(nomeCompleto.lower()))
print('Seu nome possui {} letras ao todo.'.format(len(nomeCompleto) - nomeCompleto.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nomeCompleto.find(' '))) #utilizou o find porque ele percorre o array (que começa com 0)
separa = nomeCompleto.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
