quantdias = int(input('Por quantos dias o carro foi alugado? : '))
km = float(input('Quantos Quilômetros rodados? : '))
valor = (quantdias * 60) + (km * 0.15)
print('O valor a ser pago é de R${:.2f}'.format(valor))
