#Calculadora

number1 = 0
number2 = 0
result = 0
operation = ''

number1 = float(input('Digite o primeiro número:'))
operation = input('Escolha uma operação matemática:')
number2 = float(input('Digite o segundo número:'))

if operation == '+':
    result = number1 + number2
elif operation == '-':
    result = number1 - number2
elif operation == '*':
    result = number1 * number2
elif operation == '/':
    result = number1 / number2
else:
    result = 'Operação inválida'

print(str(number1) + ' ' + str(operation) + ' ' + str(number2) + ' = ' + str(result))
      
