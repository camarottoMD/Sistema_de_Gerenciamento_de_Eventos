from add_evento import eventos
from cad_user import adicionar_participante
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
    opcao_escolhaEvento = input("Escreva o nome do evento que você deseja visualizar: ")
    eventoNome = opcao_escolhaEvento.strip().title()
    if eventoNome in eventos:
        menuEvento()
    
"""    for nome in eventos.keys():
        if eventoNome == nome:
            print('Deu certo')"""


def opcaoList():
    print("-" * 20)
    print("1 - Buscar participante: ")
    print("2 - Escolha um evento: ")
    print("3 - Voltar: ")

    escolhaOp_list = int(input("Selecione um número correspondente as opções acima: "))
    print("-" * 20)

    if escolhaOp_list == 1:
        adicionar_participante()
    elif escolhaOp_list == 2:
        pass
    elif escolhaOp_list == 3:
        menu()
    elif escolhaOp_list == 4:
        escolhaEvento()
