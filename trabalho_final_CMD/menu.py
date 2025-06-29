import os
#from add_evento import adicionar_evento
#from list_evento import listar_eventos, opcaoList
import add_evento
import list_evento
import manipulacao_user
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
    
    if escolhaOp == 1:
        list_evento.listar_eventos()
        Menu_List()
    
    elif escolhaOp == 2:
        add_evento.adicionar_evento()
    
    elif escolhaOp == 3:
        exit()
    
    else: 
        print("Opção não válida!")
        menu()
    print("-" * 20)


def Menu_List():
    while True:
        print("-" * 20)
        print("1 - Buscar participante: ")
        print("2 - Escolha um evento: ")
        print("3 - Listar temas de eventos: ") #posso colocar talvez a quantidade de eventos naquele tema
        print("4 - Voltar: ")

        opcao = int(input("Selecione um número correspondente as opções acima: "))
        print("-" * 20)
        retorno = opcao_list(opcao)
        
        if retorno is not None:
            break



def opcao_list(opcao):
    if opcao == 1:
        manipulacao_user.buscarParticipante()
    
    elif opcao == 2:
        escolhaEvento()
    
    elif opcao == 3:
        list_evento.listar_temas()
    
    elif opcao == 4:
        return ''
    
    else:
        print("Essa opção não é válida!")
        return None


def escolhaEvento():
    #global nomeEventoInput
    while True:
        nomeEventoInput = input("Escreva o nome do evento que você deseja visualizar: ")
        nomeEventoInput = nomeEventoInput.strip().title()
        
        if nomeEventoInput in add_evento.eventos:
            menu_evento.menuEvento(nomeEventoInput)
            break
        else:
            print("Esse evento não existe!")
    return nomeEventoInput

########################################################SE NO MENU EU SELECIONAR LISTAGEM ELE VAI DIRETO PRA LISTAGEM, MESMO SEM LISTA
