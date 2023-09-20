#Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la.
#Sabe-se que cada litro de tinta pinta uma área de 2m^2.

largura = float(input('Digite a largura em metros: '))
altura = float(input('Digite a altura em metros: '))
area = largura * altura
tinta = area/2

print('Sua parede tem dimensão de {}x{} e sua área é de {:.1f}m²'.format(largura, altura, area))
print('Você precisa de {:.1f} litros de tinta para pintá-la.'.format(tinta))


