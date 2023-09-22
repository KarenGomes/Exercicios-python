'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.'''
nome = input('Digite seu nome: ').lower().split()
print('Seu nome tem Silva? {}'.format('silva' in nome))