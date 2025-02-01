peso = float(input('Cual es tu peso ? (Kg) '))
altura = float(input('Cual es tu altura ? (mts) '))

imc = peso / altura **2
print('Tu indice de masa corporal es: ', int(imc))