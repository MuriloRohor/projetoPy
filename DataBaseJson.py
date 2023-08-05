import json
from Carro import Carro
from datetime import datetime

class DataBaseJson:
    NOME_ARQUIVO = "carros.json"
    LISTAJSON = list()
    LISTAOBJECT = list()

    @staticmethod
    def LerArquivo() -> list:
        arquivo = open(DataBaseJson.NOME_ARQUIVO, 'r', encoding='utf-8')
        data = arquivo.read()
        if len(data) == 0:
            return []
        data = json.loads(data)
        for c in data:
            object_carro = Carro(c['marca'], c['modelo'], c['cor'], c['ano'], c['id'])
            DataBaseJson.LISTAOBJECT.append(object_carro)
        arquivo.close()
        return DataBaseJson.LISTAOBJECT
    
    @staticmethod
    def SalvarArquivo(dados: list):
        for carro in dados:
            j = {
                    'id'    : carro.GetId(),
                    'marca' : carro.GetMarca(),
                    'modelo': carro.GetModelo(),
                    'cor'   : carro.GetCor(),
                    'ano'   : carro.GetAno()
                    }
            DataBaseJson.LISTAJSON.append(j)
        with open('log.txt', 'a') as f:
            f.write(f'\n{datetime.now()}Lista Objetos convertido para Dicionario.')

        with open(DataBaseJson.NOME_ARQUIVO, 'w+', encoding='utf-8') as arquivo:
            data = json.dumps(DataBaseJson.LISTAJSON, indent=4)
            arquivo.write(data)

                    

    




