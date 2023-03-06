print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)

segA = float(input('Primeiro segmento: '))
segB = float(input('Segundo segmento: '))
segC = float(input('Terceiro segmento: '))

if segA + segB > segC and segA + segC > segB and segB + segC > segA:
    print('\033[1:32mVocê CONSEGUE montar um triângulo com esses segmentos!!\033[m')

else:
    print('\033[1:31mVocê NÃO CONSEGUE montar um triângulo com esses segmentos!!\033[m')
