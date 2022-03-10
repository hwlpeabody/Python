#ler 5 numeros e mostrar o maior 
n1 = int(input('Escolha o primeiro número:'))
n2 = int(input('Escolha o segundo número:'))
n3 = int(input('Escolha o terceiro número:'))
n4 = int(input('Escolha o quarto número:'))
n5 = int(input('Escolha o quinto número:'))


if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
  print(f'{n1} é o maior valor!')
elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
   print(f'{n2} é o maior valor!')
elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
   print(f'{n3} é o maior valor!')
elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
  print(f'{n4} é o maior valor!')
elif n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
  print(f'{n5} é o maior valor!')
