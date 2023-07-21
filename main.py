from lerJson import *

carros = lerArquivo()


def CadastrarCarro():
    id = len(carros) + 1
    marca = input("Digite a marca do veículo: ")
    modelo = input("Digite o modelo do veículo: ")
    cor = input("Digite a cor do veículo: ")
    ano = input("Digite o ano do veículo: ")
    carro_molde = {
    "id" : id,
    "marca" : marca,
    "modelo" : modelo,
    "cor" : cor,
    "ano" : ano,
    }
    carros.append(carro_molde)
    salvarArquivo(carros)

def ListarCarros():
    for carro in carros:
        print(f"""
            Id     : {carro['id']}
            Marca  : {carro['marca']}
            Modelo : {carro['modelo']}
            Cor    : {carro['cor']}
            Ano    : {carro['ano']}
            """)

def Pausar():
    input("Pressione ENTER para continuar...")




