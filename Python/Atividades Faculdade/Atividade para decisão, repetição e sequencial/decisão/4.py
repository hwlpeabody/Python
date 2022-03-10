#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido

escolha = int(input('MENU:\n 1 - Feminino\n 2- Masculino'))

if escolha == 1:
    print('Você selecionou o gênero Feminino\n')
    
elif escolha == 2:
    print('Você selecionou o gênero Masculino\n')
            
else :
    print('Sexo inválido\n')