from add_evento import eventos, lista_temas
from cad_user import participantes
from menu import *
from menu_evento import menuEvento

def listar_eventos():
    for nome, info in eventos.items():
        print("-" * 20)
        print(f"Evento: {nome}")
        print(
            f"  Data: {info['data'].strftime('%d/%m/%Y')}"
        )  # conversao de volta para string
        print(
            f"  Horario: {info['hora'].strftime('%H:%M')}"
        )  # conversao de volta para string
        print(f"  Tema: {info['tema']}")
        print(f"  Participantes: {info['participantes']}")
        print("-" * 20)
        opcaoList()

def escolhaEvento():
    #global nomeEventoInput
    while True:
        nomeEventoInput = input("Escreva o nome do evento que você deseja visualizar: ")
        nomeEventoInput = nomeEventoInput.strip().title()
        if nomeEventoInput in eventos:
            menuEvento(nomeEventoInput)
            break
        else:
            print("Esse evento não existe!")
            
"""    for nome in eventos.keys():
        if eventoNome == nome:
            print('Deu certo')"""


def opcaoList():
    print("-" * 20)
    print("1 - Buscar participante: ")
    print("2 - Escolha um evento: ")
    print("3 - Listar temas de eventos: ") #posso colocar talvez a quantidade de eventos naquele tema
    print("4 - Voltar: ")

    escolhaOp_list = int(input("Selecione um número correspondente as opções acima: "))
    print("-" * 20)

    if escolhaOp_list == 1:
        buscarParticipante()
    elif escolhaOp_list == 2:
        escolhaEvento()
    elif escolhaOp_list == 3:
        listar_temas()
    elif escolhaOp_list == 4:
        return # porque esse return
    else:
        print("Essa opção não é válida!")
        opcaoList()    

def listar_temas():
    for tema in lista_temas:
        print("-" * 20)
        for i in lista_temas:
            print(f"{i} - {tema}")