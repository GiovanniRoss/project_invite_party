opcao = 0
while opcao != 4:

    print('''******** Programa de festa de aniversário *********
        
    [1] Adicionar convidado na lista
    [2] Remover convidado da lista
    [3] Emitir lista de convidado(s)
    [4] Sair
        
*****************************************************
    ''')
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        numero_de_convidados = int(input('\nInsira a quantidade de convidados: '))

        lista_de_convidados = []

        contador = 1

        while contador <= numero_de_convidados:
            nome_do_convidado = input(f'coloque o nome do convidado   # {contador}: ')
            lista_de_convidados.append(nome_do_convidado)
            contador+=1
        print('\n>>>>>>>>>>>>>>>>>>Convidados adicionados!!')

    elif opcao == 2:
        remover_convidado = input('Qual o convidado que deseja remover? ')
        lista_de_convidados.remove(remover_convidado)
        print('\n>>>>>>>Convidado removido<<<<<<<!!')

    elif opcao == 3:
        for nome_do_convidado in lista_de_convidados:
            print(f' \n{nome_do_convidado},você está sendo convidado para a minha festa!!')

    elif opcao == 4:
        print('...\nFim do programa!')
