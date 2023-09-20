#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros. 
#obs: Km hm dam m dm cm mm

medida = float(input('uma distância em metros: '))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
dam = medida/10
hm = medida/100
km = medida/1000

print('A medida de {}m corresponde a {}km, {}hm, {}dam, {:.0f}dm, {:.0f}cm, {:.0f}mm'.format(medida, km, hm, dam, dm, cm, mm))
