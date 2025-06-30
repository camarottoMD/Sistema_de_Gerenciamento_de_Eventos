import os
import func_evento
import func_user
import menu_evento


def limpar_tela():
    os.system("cls" if os.name == 'nt' else 'clear')

def menu():
    #limpar_tela()
    print("1 - Listagem de Eventos")
    print("2 - Adicionar Evento")
    print("3 - Sair")
    escolhaOp = int(input("Selecione um número correspondente as opções acima: "))
    opcaoMenu(escolhaOp)


def opcaoMenu(escolhaOp):
    match escolhaOp:
        case 1:
            func_evento.listar_eventos()
            Menu_List()
        case 2:
            func_evento.adicionar_evento()
        case 3:    
            exit()
        case _:
            print("Opção não válida!")
            menu()
            print("-" * 20)


def Menu_List():

    print("-" * 20)
    print("1 - Buscar participante: ")
    print("2 - Escolha um evento: ")
    print("3 - Listar temas de eventos: ") #posso colocar talvez a quantidade de eventos naquele tema
    print("4 - Voltar: ")

    opcao = int(input("Selecione um número correspondente as opções acima: "))
    print("-" * 20)

    match opcao: #pesquisar depois
        case 1: 
            func_user.buscarParticipante()
        case 2:
            escolhaEvento()
        case 3:
            func_evento.listar_temas()
        case _:
            print("opção inválida")

def escolhaEvento():
    #global nomeEventoInput
    while True:
        nomeEventoInput = input("Escreva o nome do evento que você deseja visualizar: ")
        nomeEventoInput = nomeEventoInput.strip().title()
        
        if nomeEventoInput in func_evento.eventos:
            menu_evento.menuEvento(nomeEventoInput)
            break
        else:
            print("Esse evento não existe!")
    return nomeEventoInput

########################################################SE NO MENU EU SELECIONAR LISTAGEM ELE VAI DIRETO PRA LISTAGEM, MESMO SEM LISTA
