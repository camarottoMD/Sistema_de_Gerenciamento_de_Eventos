from func_user import *
from func_evento import *

def listar_evento_unico(nome_evento):
    info = eventos[nome_evento]
    nome = nome_evento
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


def menuEvento(nome_evento):

    while True:
        print("1 - Adicionar participante")
        print("2 - Editar evento")
        print("3 - Voltar")
        try:
            opcao = input("Selecione um número correspondente as opções acima: ")
            if not opcao.isdigit():
                print("Por favor, digite um número válido.")
                continue
            opcao = int(opcao)
            Opcao_Evento(opcao, nome_evento)
            break
        except Exception as e:
            print(f"Erro no menu do evento: {e}")
            continue



def Opcao_Evento(opcao, nome_evento):
    try:
        if opcao == 1:
            try:
                adicionar_participante(nome_evento)
            except Exception as e:
                print(f"Erro ao adicionar participante: {e}")
        elif opcao == 2:
            try:
                editar_evento()
            except Exception as e:
                print(f"Erro ao editar evento: {e}")
        elif opcao == 3:
            return
        else:
            print("Opção não válida!")
            menuEvento(nome_evento)
            print("-" * 20)
    except Exception as e:
        print(f"Erro na opção do evento: {e}")