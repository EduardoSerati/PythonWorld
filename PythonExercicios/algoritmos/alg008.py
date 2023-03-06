metros = float(input('Digite uma distância em metros: '))

km = metros / 1000
dm = metros * 10
cm = metros * 100
mm = metros * 1000
mc = metros * 1000000
nm = metros * 1000000000
angstrom = metros * 10000000000

print('A distância de {}m corresponde a: '.format(metros))
print('{}Km'.format(km))
print('{:.0f}dm'.format(dm))
print('{:.0f}cm'.format(cm))
print('{:.0f}mm'.format(mm))
print('{:.0f}mc'.format(mc))
print('{:.0f}nm'.format(nm))
print('{:.0f}Å'.format(angstrom))
