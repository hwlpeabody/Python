#nota entre 0 e 10
nota = float(input('Digite sua nota:'))

while (nota>10) or (nota<0):
  nota = float(input('Digite sua nota:'))
print(nota)