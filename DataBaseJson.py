import json

class DataBaseJson:
    NOME_ARQUIVO = "carros.json"

    @staticmethod
    def LerArquivo():
        arquivo = open(DataBaseJson.NOME_ARQUIVO, 'r', encoding='utf-8')
        data = arquivo.read()
        if len(data) == 0:
            return []
        data = json.loads(data)
        arquivo.close()
        return data
    
    @staticmethod
    def SalvarArquivo(dados):
        with open(DataBaseJson.NOME_ARQUIVO, 'w+', encoding='utf-8') as arquivo:
            data = json.dumps(dados, indent=4)
            arquivo.write(data)
    




