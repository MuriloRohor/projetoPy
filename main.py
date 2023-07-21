from lerJson import *

carros = lerArquivo()


def CadastrarCarro():
    marca = input("Digite a marca do veículo: ")
    modelo = input("Digite o modelo do veículo: ")
    cor = input("Digite a cor do veículo: ")
    ano = input("Digite o ano do veículo: ")
    carro_molde = {
    "marca" : marca,
    "modelo" : modelo,
    "Cor" : cor,
    "Ano" : ano,
    }
    carros.append(carro_molde)
    salvarArquivo(carros)







