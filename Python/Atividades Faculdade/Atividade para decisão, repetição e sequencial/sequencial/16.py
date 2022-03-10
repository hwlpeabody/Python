#pedir o tamanho em metros quadrados da área a ser pintada
#1 litro para cada 3 metros quadrados e é vendida em latas de 18 litros que custa 80 reais 
#nformar ao usuário a qntd de latas de tinta a serem comprada e o preço total

metros2 = float(input('Valor em metros quadrados da área a ser pintada: '))
litro = metros2 / 3
preço_lata = 80
quantidade_litros_lata = 18

latas = (litro / quantidade_litros_lata)
total = (latas * preço_lata)

print(f'Você usará {latas} latas de tinta \n O total da compra é: R${total}')






