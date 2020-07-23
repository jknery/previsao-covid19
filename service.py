from machine_learning import Neuronio
from graphics import Grafico
from tratamento_dados import TratamentoDados


class Service:

    def predictingInDays(self):

        tratamento = TratamentoDados()

        tratamento.tratamentoDadosAcumulados()

        dias = tratamento.getDias()
        casos = tratamento.getCasos()
        obitos = tratamento.getObitos()

        numero_dias_predicao = 10

        neuronio = Neuronio(dias, casos, obitos)

        neuronio.predictingCasos(numero_dias_predicao)
        neuronio.predictingObitos(numero_dias_predicao)

        proximos_dias = neuronio.getProximosDias()
        previsao_casos = neuronio.getPrevisaoCasos()
        previsao_obitos = neuronio.getPrevisaoObitos()

        grafico = Grafico(dias, casos)

        grafico.plotGraficoAcumulo(obitos, numero_dias_predicao, previsao_casos,
                                   proximos_dias, previsao_obitos)

    def showByDays(self):

        tratamento = TratamentoDados()
        tratamento.tratamentoDadosPorDia()

        dias = tratamento.getDias()
        casos = tratamento.getCasos()

        grafico = Grafico(dias, casos)

        grafico.plotGraficoPorDia()

    def showByRegioes(self):

        tratamento = TratamentoDados()
        tratamento.tratamentoDadosPorRegioes()

        dias = tratamento.getDias()
        casos = tratamento.getCasos()
        regioes = tratamento.getRegioes()
        porcento = tratamento.getPorcento()

        grafico = Grafico(dias, casos)

        grafico.plotGraficoPorRegiao(regioes)
