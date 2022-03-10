#perguntar quanto ganha por hora e o número de horas trabalhadas no mes
#mostrar o total do salario no mes referido
# é descontado 11% para o imposto de renda, 8% para o inss e 5% para o sindicato
# 1- salario bruto, 2- quanto pagou ao inss, 3- quanto pagou ao sindicato, 4- salario liquido
# 5- calcular os descontos e o salaro liquido conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

valor_por_hora = float(input('Valor por hora: '))
dias = int(input('Dias trabalhados por semana: '))
horas = float(input('Horas por dia: '))
horas_trabalhadas_mes = (dias * horas * 4)
valor_mensal = (valor_por_hora * horas_trabalhadas_mes)
ir = (valor_mensal * 11/100)
inss =  (valor_mensal * 8/100)
sindicato = (valor_mensal * 5/100)
salario_liquido =  (valor_mensal - ir - inss - sindicato )

print(f'Salário bruto: R${valor_mensal} \n Imposto de renda(11%): R${ir} \n INSS(8%): R${inss} \n Sindicato(5%): R$:{sindicato} \n Salário liquido: R${salario_liquido}')
