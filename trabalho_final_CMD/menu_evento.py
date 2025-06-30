from func_user import *
from func_evento import *


def listar_evento_unico(nomeEventoInput):
    info = eventos[nomeEventoInput] 
    nome = nomeEventoInput # por que aqui nao posso usar for, e porque nao posso acessar os items()
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
    return nome, info


def menuEvento(nome):
    listar_evento_unico(nome)

    print("1 - Adicionar participante")
    print("2 - Editar evento")
    print("3 - Voltar")

    opcao = int(
        input("Selecione um número correspondente as opções acima: ")
    )

    Opcao_Evento(opcao, nome)



def Opcao_Evento(opcao, nome):
    match opcao:
        case 1:
            adicionar_participante(nome)
        case 2:
            editar_evento()
        case 3:
            return
    
        case _:
            print("Opção não válida!")
            menuEvento()
            print("-" * 20)