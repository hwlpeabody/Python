#Peso ideal
sexo = input('Você é homem(1) ou mulher(2)?')
altura = float(input('Para saber seu peso ideal digite sua altura em cm:'))

if sexo == '1':
    print((72.7 * altura) - 58)
elif sexo == '2':
    print((62.1 * altura) - 44.7)