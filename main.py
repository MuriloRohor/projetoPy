from DataBaseJson import DataBaseJson
from Carro import Carro

LISTA_CARROS = DataBaseJson.LerArquivo()

class Controller:
    
    @staticmethod
    def Cadastrar():
        marca = input("Digite a marca do veículo: ")
        modelo = input("Digite o modelo do veículo: ")
        cor = input("Digite a cor do veículo: ")
        ano = input("Digite o ano do veículo: ")
        id = len(LISTA_CARROS) + 1
        object_carro = Carro(marca, modelo, cor, ano, id)
        LISTA_CARROS.append(object_carro)
        DataBaseJson.SalvarArquivo(LISTA_CARROS)
    
    @staticmethod
    def Listar():
        for carro in LISTA_CARROS:
            print('\n')
            print(f"Id: {carro.GetId()}\nMarca: {carro.GetMarca()}\nModelo: {carro.GetModelo()}\nCor: {carro.GetCor()}\nAno: {carro.GetAno()}")

    @staticmethod
    def Excluir():
        id_select = int(input("Digite o ID do veículo que deseja excluir: "))
        for i, e in enumerate(LISTA_CARROS):
            if e.GetId() == id_select:
                LISTA_CARROS.pop(i)
                DataBaseJson.SalvarArquivo(LISTA_CARROS)
                print("Veículo excluído com sucesso!")
    @staticmethod
    def SelecionarPorId():
        id_select = int(input("Digite o ID do veículo que deseja selecionar: "))
        for i in LISTA_CARROS:
            if i.GetId() == id_select:
                print(f"""
                Id     : {i.GetId()}
                Marca  : {i.GetMarca()}
                Modelo : {i.GetModelo()}
                cor    : {i.GetCor()}
                ano    : {i.GetAno()}
                """)