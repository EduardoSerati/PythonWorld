from time import sleep
from random import randint

computador = randint(0, 5)

print('-=-' * 30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 30)

jogador = int(input('Em que número eu pensei? '))
print('Analisando...')
sleep(2)

if jogador == computador:
    print('Você adivinhou o número. PARABÉNS!!')

else:
    print('Você errou o número. Eu pensei no {} e não no {}. Tente Novamente!'.format(computador, jogador))
