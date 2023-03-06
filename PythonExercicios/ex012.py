value = float(input('Quanto custa o produto? : R$'))
discount = value - (value * 5 / 100)
print('O valor do produto é de R${:.2f}, mas com o desconto de 5%, o novo valor agora será de R${:.2f}'.format(value, discount))
