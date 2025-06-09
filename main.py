from list_evento import *
from add_evento import *

def menu():
    print("1 - Listagem de Eventos")
    print("2 - Adicionar Evento")
    print("3 - Sair")
    opcaoMenu()


def opcaoMenu():
    escolhaOp = int(input("Selecione um número correspondente as opções acima: "))
    if escolhaOp == 1:
        listar_eventos()
    elif escolhaOp == 2:
        adicionar_evento()
    elif escolhaOp == 3:
        exit()


while True:
    menu()