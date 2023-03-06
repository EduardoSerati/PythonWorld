from math import cos, sin, tan, radians

ang = float(input('Digite algum ângulo: '))
cos = cos(radians(ang))
sin = sin(radians(ang))
tan = tan(radians(ang))
print('O ângulo de {}° tem o COSSENO de {:.2f}'.format(ang, cos))
print('O ângulo de {}° tem o SENO de {:.2f}'.format(ang, sin))
print('O ângulo de {}° tem a TANGENTE de {:.2f}'.format(ang, tan))
