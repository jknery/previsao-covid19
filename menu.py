
class Menu:

    def menuPrincipal(self):

        print()
        print("############################################")
        print("#     Sistema de Predição do Covid-19      #")
        print("############################################")
        print("# 01 - Predição de Casos e Óbitos          #")
        print("# 02 - Qntd. Casos por Dia                 #")
        print("# 03 - Gráfico por Região                  #")
        print("# 04 - Encerra o Programa                  #")
        print("############################################")
        opcao = int(input("Digite a Opção escolhida: "))
        print()
        return opcao
