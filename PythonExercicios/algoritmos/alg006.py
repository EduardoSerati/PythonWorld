num = int(input('Digite um número: '))
suc = num + 1
ant = num - 1
print('\033[1:34mO antecessor de {} é {}\033[m'.format(num, ant))
print('\033[1:34mO sucessor de {} é {}\033[m'.format(num, suc))
