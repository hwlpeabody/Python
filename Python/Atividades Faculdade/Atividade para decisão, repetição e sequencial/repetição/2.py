#pedir nome de usuário e senha porém senha diferente do nome

nome = input('Digite o nome do usuário: ')
senha = input('Digite uma senha: ')

while (nome.lower() == senha.lower()):
  senha= input('Escolha uma nova senha: ')
else: 
  print('Cadastro efetuado!')