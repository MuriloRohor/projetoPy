import json

NOME_ARQUIVO = "carros.json"

def lerArquivo():
    arquivo = open(NOME_ARQUIVO, 'r', encoding='utf-8')
    data = arquivo.read()
    if len(data) == 0:
        return []
    data = json.loads(data)
    arquivo.close()
    return data

def salvarArquivo(dados):
    arquivo = open(NOME_ARQUIVO, 'w+', encoding='utf-8')
    data = json.dumps(dados, indent=4)
    arquivo.write(data)
    arquivo.close()
    




