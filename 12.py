#faça um algoritmo que leia um preço de um produto e mostre seu novo preço, com desconto de 5%.

valor = float(input('Digite o preço do produto: '))
desconto = valor * (5/100)

print('O valor do produto com desconto é de {:.2f}R$'.format(valor - desconto))