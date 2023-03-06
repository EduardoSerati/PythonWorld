name = str(input('Digite o seu nome completo: ')).strip()
separa = name.split()

print('Seu nome em MAIÚSCULAS = {}'.format(name.upper()))
print('Seu nome em minúsculas = {}'.format(name.lower()))
print('Seu nome tem {} letras'.format(len(name) - name.count(' ')))
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))
