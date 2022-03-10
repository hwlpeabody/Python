#Questão1
#notebook = 1500, tablet = 1000



print('Olá! Seja bem vindo a Zenith, a loja onde você vai achar itens de tecnologia pelos melhores valores.')

resultado = input('Deseja fazer seu cadastro na Zenith?') #só pode escolher sim no momento pq eu ainda não aprendi a finalizar no caso de não e a continuar no caso de sim

if resultado.lower() == 'sim': #.lower()(é para deixar tudo minusculo) e .upper()(para ficar tudo maiusculo)
    nome = input('Digite seu nome:')
elif resultado.lower() != 'não':
    print('Uma pena você não se cadastrar porém a Zenith estará sempre de portas abertas') 

data_de_nascimento = input('Qual a data do seu nascimento?') #não sei como parar então botei isso para dar erro e acabar
país = input('Qual o pais que você mora?')
cpf = input('Digite seu cpf, caso não queira digite "não:"')
notebook = float(input('Olá {}! Quantos notebooks você irá querer?'.format(nome)))
notebook_valor = (1500 * notebook)
tablet = float(input('Quantos tablets você irá querer?'))
tablet_valor = (1000 * tablet)
total = (notebook + tablet)
valor = float
valor_inicial = float(notebook_valor + tablet_valor)

if total < 3:
    valor = (notebook_valor + tablet_valor)
elif total >= 3:
    valor = (notebook_valor + tablet_valor - 500)

pagamento = (input('O pagamento sera à vista(1) ou parcelado(2)?'))
a_vista = float(valor - (valor* 0.1)) #jeito 1 #aprender 
parcelado = float(valor + (valor * 8/100)) #jeito 2

print('O valor da compra antes da aplicação da promoção é: {:.2f}' .format(valor_inicial)) #{:.2f}= ponto 2 float
print( 'O valor da compra depois da aplicação da promoção é: {:.2f}' .format(valor))

if pagamento == '1':
    print('O valor depois da aplicação da forma de pagamento é {:.2f}:' .format(a_vista))
elif pagamento == '2':
    print('O valor depois da aplicação da forma de pagamento é {:.2f}:' .format(parcelado))

