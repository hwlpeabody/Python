#cliente comprar frutas
#morangos até 5kg = 2.50 por kg / morangos acima de 5kg = 2.20
#maçãs até 5kg = 1.80 por kg / maçãs acima de 5kg = 1.50

#Variáveis: mp1 = morango preço 1, mçp1 = maça preço 1, mp2 = morango preço 2, mçp2 = maça preço 2, tk = total kilos, tp = total preço, vf = valor final

#compras 
morangos = float(input('Quantos kilos de morango você irá querer? '))
mp1 = float(morangos * 2.50)
mp2 = float(morangos * 2.20)
maças = float(input('Quantos kilos de maçã você irá querer? '))
mçp1 = float(maças * 1.80)
mçp2 = float(maças * 1.50)
tk = float(morangos + maças)
tp1 = float(mp1 + mçp1)  
tp2 = float(mp2 + mçp2)

if tk <= 5:
    sla= tp1 
elif tk > 5:
    sla = tp2


if tk > 8 or sla > 25:
    vf = float(sla - (sla * 10/100))
elif tk <= 8 or sla <= 25:
    vf = float( sla)
    
print(vf)