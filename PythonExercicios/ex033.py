value1 = int(input('Primeiro valor: '))
value2 = int(input('Segundo valor: '))
value3 = int(input('Terceiro valor: '))

maior = value1

if value2 > value1 and value2 > value3:
    maior = value2

if value3 > value1 and value3 > value2:
    maior = value3

menor = value1

if value2 < value1 and value2 < value3:
    menor = value2

if value3 < value1 and value3 < value2:
    menor = value3

print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))
