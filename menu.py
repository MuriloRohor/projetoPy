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
<<<<<<< HEAD
        Pausar()
=======
        input("Pressione ENTER para continuar... ")
>>>>>>> 3e21d05e43732b9f3fd3e224a45e06f755c66d0b
        
        
    
    if opcao == 1:
        CadastrarCarro()
        print("Carro cadastrado com sucesso!")
<<<<<<< HEAD
        Pausar()

    elif opcao == 2:
        ListarCarros()
        Pausar()
=======

    elif opcao == 2:
        pass
>>>>>>> 3e21d05e43732b9f3fd3e224a45e06f755c66d0b
    
    elif opcao == 3:
        pass

    elif opcao == 4:
        pass

    elif opcao == 0:
        print("Encerrando...")
        break

    else:
        print("Insira uma opcao válida.")
<<<<<<< HEAD
        Pausar()
=======
        input("Pressione ENTER para continuar... ")
>>>>>>> 3e21d05e43732b9f3fd3e224a45e06f755c66d0b
