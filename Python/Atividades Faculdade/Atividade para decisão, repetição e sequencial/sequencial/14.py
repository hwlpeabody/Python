#se joão trouxer mais de 50kg de peixe deve pagar uma multa de 4 reais por kg excedente

peso = float(input('Quantos kg de peixe joão trouxe? '))
excesso = (peso - 50)
multa = ((excesso) * 4)

if peso > 50:
    print(f'Você irá pagar R$:{multa :.2f} de multa.')
elif peso < 50:
    print('Você não irá pagar multa')