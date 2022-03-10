#somar media de 5 valores e depois mostrar a soma e a media

v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
v3 = int(input('Digite o terceiro valor: '))
v4 = int(input('Digite o quarto valor: '))
v5 = int(input('Digite o quinto valor: '))

soma_dos_valores = (v1 + v2 + v3 + v4 + v5)
media = (soma_dos_valores / 5)

print(f'A soma dos valores é: {soma_dos_valores}')
print(f'A média é: {media}')