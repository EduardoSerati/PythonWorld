salário = float(input('Qual é o salário do funcionário? '))

if salário > 1250:
    aumento = salário + (salário * 10/100)

else:
    aumento = salário + (salário * 15/100)

print('O salário de R${:.2f}, agora será de R${:.2f}'.format(salário, aumento))
