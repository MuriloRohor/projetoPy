class Carro:
    id: int
    marca: str
    modelo: str
    cor: str
    ano: str
    
    def __init__(self,marca, modelo, cor, ano, id) -> None:
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def GetId(self):
        return self.id
    
    def GetMarca(self):
        return self.marca
    
    def GetModelo(self):
        return self.modelo
    
    def GetCor(self):
        return self.cor
    
    def GetAno(self):
        return self.ano
    