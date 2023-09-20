#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#considere US$1 = R$3,27

real = float(input('Digite quanto você possui na carteira: '))
dolar = real/3.27

print('Com R${} você pode comprar US${:.2f}'.format(real, dolar))