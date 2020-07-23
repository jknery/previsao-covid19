import json
from extrai_dados import ExtraiDados


class TratamentoDados(ExtraiDados):

    dias = []
    casos = []
    obitos = []
    regioes = []
    porcento = []

    def __init__(self):
        super().__init__()

    def tratamentoDadosAcumulados(self):

        results = json.loads(super().load_covid_data_acumulado())['results']

        results = list(map(lambda i: {
            'dia': i['label'],
            'casos': i['qtd_confirmado'],
            'obitos': i['qtd_obito']
        }, results))

        self.dias = range(1, len(results) + 1)
        self.casos = list(map(lambda i: i['casos'], results))
        self.obitos = list(map(lambda i: i['obitos'], results))

    def tratamentoDadosPorDia(self):

        results = json.loads(super().load_covid_data_por_dia())['results']

        results = list(map(lambda i: {
            'dia': i['label'],
            'casos': i['qtd_confirmado']
        }, results))

        self.dias = range(1, len(results) + 1)
        self.casos = list(map(lambda i: i['casos'], results))

    def tratamentoDadosPorRegioes(self):

        results = json.loads(super().load_covid_por_regiao())['results']

        results = list(map(lambda i: {
            'regiao': i['nome'],
            'casos': i['qtd'],
            'porcento': i['percent']
        }, results))

        self.regioes = list(map(lambda i: i['regiao'], results))
        self.casos = list(map(lambda i: i['casos'], results))
        self.porcento = list(map(lambda i: i['porcento'], results))

    def getDias(self):
        return self.dias

    def getCasos(self):
        return self.casos

    def getObitos(self):
        return self.obitos

    def getRegioes(self):
        return self.regioes

    def getPorcento(self):
        return self.porcento
