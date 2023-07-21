from main import *
opcao = None

while opcao != 0:
    print("""
        1 - Cadastrar Veiculos
        2 - Listar Veículos
        3 - Editar Veículos
        4 - Remover Veículos
        0 - Sair
    """)

    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Insira um número válido.")

        Pausar()

        input("Pressione ENTER para continuar... ")

        
        
    
    if opcao == 1:
        CadastrarCarro()
        print("Carro cadastrado com sucesso!")

        Pausar()

    elif opcao == 2:
        ListarCarros()
        Pausar()


    elif opcao == 2:
        pass

    
    elif opcao == 3:
        pass

    elif opcao == 4:
        pass

    elif opcao == 0:
        print("Encerrando...")
        break

    else:
        print("Insira uma opcao válida.")

        Pausar()

        input("Pressione ENTER para continuar... ")

