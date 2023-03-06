Money = float(input('Quanto dinheiro você tem na carteira? R$'))
ToDolar = Money / 5.24
ToEuro = Money / 5.54
ToLibra = Money / 6.23
ToYen = Money / 0.0387
print('Com R${:.2f}, Você pode comprar: ${:.2f}'.format(Money, ToDolar))
print('Com R${:.2f}, Você pode comprar: {:.2f} €'.format(Money, ToEuro))
print('Com R${:.2f}, Você pode comprar: £{:.2f}'.format(Money, ToLibra))
print('Com R${:.2f}, Você pode comprar: ￥{:.2f}'.format(Money, ToYen))
