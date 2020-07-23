from menu import Menu
from service import Service

status = 0
menu = Menu()
service = Service()

while status != 4:

    status = menu.menuPrincipal()

    if status == 1:
        service.predictingInDays()

    elif status == 2:
        service.showByDays()

    elif status == 3:
        service.showByRegioes()

    elif status == 4:
        print("Good Bye!")

    else:
        print("Você digitou qualquer outra coisa....Digite entre 1 e 4")
