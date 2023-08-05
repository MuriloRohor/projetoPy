from main import *
opcao = None

while opcao != 0:
    print("""
        1 - Cadastrar Veiculo
        2 - Listar Veículos
        3 - Selecionar Veículo
        4 - Editar Veículo
        5 - Remover Veículo
        0 - Sair
    """)

    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Insira um número válido.")

        Pausar()

        input("Pressione ENTER para continuar... ")

        
        
    
    if opcao == 1:
        Controller.Cadastrar()
        Pausar()

    elif opcao == 2:
        Controller.Listar()
        Pausar()

    elif opcao == 2:
        pass
    
    elif opcao == 3:
        SelecionarVeiculoId()
        Pausar()

    elif opcao == 4:
        ExcluirCarro()
        Pausar()

    elif opcao == 0:
        print("Encerrando...")
        break

    else:
        print("Insira uma opcao válida.\n")
        Pausar()


