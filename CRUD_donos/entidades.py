from datetime import datetime, date
formatacaoParaData = "%d/%m/%Y"
dataDoSistema = date.today()

class Tutor:

    def __init__(self,nome,dataDeNascimento,endereco,cidade,estado):
        self.nome = nome
        self.dataDeNascimento = (datetime.strptime(dataDeNascimento, formatacaoParaData)).date()
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado
        self.idade = (dataDoSistema - self.dataDeNascimento).days//365
        return
