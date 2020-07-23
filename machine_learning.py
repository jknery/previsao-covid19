# Fitting Polynomial Regression to the dataset
from numpy import *
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


class Neuronio:

    previsao_obitos = []
    previsao_casos = []
    proximos_dias = []

    def __init__(self, dias, casos, obitos):
        self.dias = dias
        self.casos = casos
        self.obitos = obitos

    def predictingCasos(self, n_dias):

        # Treinando o modelo de regressão
        dias_anteriores = list(zip(self.dias,  self.dias))

        poly = PolynomialFeatures(degree=4)
        dias_anteriores = poly.fit_transform(dias_anteriores)

        poly.fit(dias_anteriores,  self.casos)
        lin2 = LinearRegression()
        lin2.fit(dias_anteriores,  self.casos)

        # Prevendo N dias para frente
        ultimo_dia = self.dias[-1]
        self.proximos_dias = range(ultimo_dia, ultimo_dia + n_dias)
        self.proximos_dias = list(zip(self.proximos_dias, self.proximos_dias))
        self.previsao_casos = lin2.predict(
            poly.fit_transform(self.proximos_dias))

    def predictingObitos(self, n_dias):

        # Treinando o modelo de regressão
        dias_anteriores = list(zip(self.dias,  self.dias))

        poly = PolynomialFeatures(degree=4)
        dias_anteriores = poly.fit_transform(dias_anteriores)

        poly.fit(dias_anteriores,  self.obitos)
        lin2 = LinearRegression()
        lin2.fit(dias_anteriores,  self.obitos)

        # Prevendo N dias para frente
        ultimo_dia = self.dias[-1]
        self.proximos_dias = range(ultimo_dia, ultimo_dia + n_dias)
        self.proximos_dias = list(zip(self.proximos_dias, self.proximos_dias))
        self.previsao_obitos = lin2.predict(
            poly.fit_transform(self.proximos_dias))

    def getProximosDias(self):
        return self.proximos_dias

    def getPrevisaoCasos(self):
        return self.previsao_casos

    def getPrevisaoObitos(self):
        return self.previsao_obitos
