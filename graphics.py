import pylab


class Grafico:

    def __init__(self, dias, casos):
        self.dias = dias
        self.casos = casos

    def plotGraficoAcumulo(self, obitos, num_dias, previsao_casos, proximos_dias, previsao_obitos):

        pylab.plot(self.dias,  self.casos, '-b', marker='o',
                   markersize=4, label='Casos')

        pylab.plot(self.dias,  obitos, '-r', marker='*',
                   markersize=4, label='Óbitos')

        pylab.plot(proximos_dias,  previsao_casos, color='yellow',
                   marker='o', markersize=4, label='Previsão de Casos')

        pylab.plot(proximos_dias,  previsao_obitos, color='orange',
                   marker='*', markersize=4, label='Previsão de Obitos')

        pylab.legend(loc='upper left')
        pylab.title(
            'Predição de Casos no Brasil para os próximos ' + str(num_dias) + ' dias')
        pylab.xlabel('Qntd. Dias')
        pylab.ylabel('Qntd. Casos/Óbitos')
        pylab.show()

    def plotGraficoPorDia(self):

        pylab.plot(self.dias, self.casos, '-b', marker='o',
                   markersize=4, label='Casos')

        pylab.legend(loc='upper left')
        pylab.title('Casos confirmados por dia no Brasil')
        pylab.xlabel('Qntd. Dias')
        pylab.ylabel('Qntd. Casos')
        pylab.show()

    def plotGraficoPorRegiao(self, regioes):

        fig = pylab.figure()
        ax = fig.add_axes([0, 0, 1, 1])
        ax.axis('equal')
        ax.pie(self.casos, labels=regioes, autopct='%1.2f%%')
        pylab.legend(loc='upper left')
        pylab.title('Casos confirmados por Região no Brasil')
        pylab.show()
