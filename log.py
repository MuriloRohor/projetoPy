from datetime import datetime

def RegistroLog(n: int, info=None):
    tipo = n
    while True:
        if n == 1:
            with open('log.txt', 'a') as f:
                f.write(f'\n{datetime.now()} - Ambiente Controller -> Objeto Adicionado a lista <LISTA_CARROS> - ID: {info.GetId()} / MARCA: {info.GetMarca()} / MODELO: {info.GetModelo()} / COR: {info. GetCor()} / ANO: {info.GetAno()}')
                break
        if n == 2:
            with open('log.txt', 'a') as f:
                f.write(f'\n{datetime.now()} - Ambiente Controller -> Objeto selecionado para exclusão - ID: {info.GetId()} / MARCA: {info.GetMarca()} / MODELO: {info.GetModelo()} / COR: {info. GetCor()} / ANO: {info.GetAno()}')
                break

        if n == 3:
            pass

        if n == 4:
            with open('log.txt', 'a') as f:
                f.write(f'\n{datetime.now()} - Ambiente DataBaseJson -> Falha ao converter Objeto para Json e adicionar na lista <LISTA_JSON>')
                break

        if n == 5:
            with open('log.txt', 'a') as f:
                f.write(f'\n{datetime.now()} - Ambiente DataBaseJson -> Objeto convertida para Json e adicionado na lista <LISTA_JSON> com sucesso!.')
                break
        if n == 6:
            pass 
