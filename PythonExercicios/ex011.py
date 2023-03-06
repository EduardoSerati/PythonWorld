larg = float(input('Quanto de Largura tem a parede? : '))
alt = float(input('Quanto de Altura tem a parede? : '))
areaQuad = larg * alt
tinta = areaQuad / 2
print('As dimensões da parede é {}x{} e sua área é de {}m²'.format(larg, alt, areaQuad))
print('Para pintar toda essa parede, você precisará de {}l'.format(tinta))
