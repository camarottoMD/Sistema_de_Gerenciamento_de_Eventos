from cad_user import *

def menuEvento():

    print("1 - Adicionar participante")
    print("2 - Editar evento")
    print("3 - Voltar")
    opcaoMenu_evento()

def opcaoMenu_evento():
    escolhaOp_evento = int(input("Selecione um número correspondente as opções acima: "))
    if escolhaOp_evento == 1:
        cad_user()
    elif escolhaOp_evento == 2:
        pass
    elif escolhaOp_evento == 3:
        exit()
    else: 
        print("Opção não válida!")
        menuEvento()
    print("-" * 20)