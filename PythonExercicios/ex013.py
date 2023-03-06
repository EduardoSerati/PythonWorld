salário = float(input('Qual é o salário? : R$'))
aumento = salário + (salário * 15 / 100)
print('O salário do funcionário é de R${:.2f}'
      ' mas com o novo aumento de 15%, será de R${:.2f}'
      .format(salário, aumento))
