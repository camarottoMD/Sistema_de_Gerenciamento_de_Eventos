from cad_user import *
from add_evento import eventos


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
    if opcao == 1:
        adicionar_participante(nome)
    
    elif opcao == 2:
        return None
    
    elif opcao == 3:
        return #porque usar return
    
    else:
        print("Opção não válida!")
        menuEvento()
    print("-" * 20)