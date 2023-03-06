vel = float(input('Qual a velocidade atual do carro? '))

if vel <= 80:
    print('Velocidade de {}Km/h permitida!.'.format(vel))

else:
    multa = (vel - 80) * 7
    print('Velocidade de {}Km/h . ACIMA DA VELOCIDADE PERMITIDA! Multa aplicada de R${:.2f}'.format(vel, multa))
    
print('Tenha um bom dia! Dirija com segurança')
