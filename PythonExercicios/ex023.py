value = int(input('Digite um número: '))
u = value // 1 % 10
d = value // 10 % 10
c = value // 100 % 10
m = value // 1000 % 10

print('Seu número é {} e tem:'.format(value))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
