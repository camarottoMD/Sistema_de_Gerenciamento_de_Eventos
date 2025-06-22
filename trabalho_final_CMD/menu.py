import os
from add_evento import adicionar_evento
from list_evento import *

def limpar_tela():
    os.system("cls" if os.name == 'nt' else 'clear')

def menu():
    #limpar_tela()
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
    else: 
        print("Opção não válida!")
        menu()
    print("-" * 20)



