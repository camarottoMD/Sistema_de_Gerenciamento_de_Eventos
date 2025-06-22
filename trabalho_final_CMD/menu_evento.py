from cad_user import *
from add_evento import *


def listar_evento_unico():
    for nome, info in eventos[nome_evento].items(): # aqui eu tive que usar o for e nao o if
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


def menuEvento():
    listar_evento_unico()

    print("1 - Adicionar participante")
    print("2 - Editar evento")
    print("3 - Voltar")
    opcaoMenu_evento()


def opcaoMenu_evento():
    escolhaOp_evento = int(
        input("Selecione um número correspondente as opções acima: ")
    )
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