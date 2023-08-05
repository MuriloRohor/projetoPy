from DataBaseJson import DataBaseJson
import Carro

LISTA_CARROS = DataBaseJson.LerArquivo()

class Controller:
    
    @staticmethod
    def Cadastrar():
        marca = input("Digite a marca do veículo: ")
        modelo = input("Digite o modelo do veículo: ")
        cor = input("Digite a cor do veículo: ")
        ano = input("Digite o ano do veículo: ")
        LISTA_CARROS.append(Carro(marca, modelo, cor, ano))
    
    @staticmethod
    def Listar():
        for carro in LISTA_CARROS:
            print(f"Id: {carro.GetId}\nMarca: {carro.GetMarca}\nModelo: {carro.GetModelo}\nCor: {carro.GetCor}\nAno: {carro.GetAno}")


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
    DataBaseJson.SalvarArquivo(carros)

def ListarCarros():
    for carro in carros:
        print(f"""
            Id     : {carro['id']}
            Marca  : {carro['marca']}
            Modelo : {carro['modelo']}
            Cor    : {carro['cor']}
            Ano    : {carro['ano']}
            """)
        
def ExcluirCarro():
    id_select = int(input("Digite o ID do veículo que deseja excluir: "))
    for i, e in enumerate(carros):
        if e['id'] == id_select:
            carros.pop(i)
            DataBaseJson.SalvarArquivo(carros)
            print("Veículo excluído com sucesso!")

def SelecionarVeiculoId():
    id_select = int(input("Digite o ID do veículo que deseja selecionar: "))
    for carro in carros:
        if carro['id'] == id_select:
            print(f"""
            Id     : {carro['id']}
            Marca  : {carro['marca']}
            Modelo : {carro['modelo']}
            cor    : {carro['cor']}
            ano    : {carro['ano']}
            """)
            
        

def Pausar():
    input("Pressione ENTER para continuar...")




