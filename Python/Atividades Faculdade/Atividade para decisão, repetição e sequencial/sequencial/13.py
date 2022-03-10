#construir um algoritimo que calcule o peso ideal da pessoa de acordo com a altura
# usando as formulas  "(72.7 * h) - 58" para homens e "(62.1 * h - 44.7)" para mulheres

print('Saber seu peso ideal com base na sua altura')

h = float(input('Sua altura: '))
sexo = int(input('Masculino[1] \n Feminino[2] \n'))
 
if sexo == 1:
    print((72.7 * h) - 58)
elif sexo == 2:
    print((62.1 * h ) - 44.7)

