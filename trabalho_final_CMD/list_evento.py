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


"""for nome in eventos.keys():
        if eventoNome == nome:
            print('Deu certo')"""

def listar_temas():
    print("-" * 20)
    for tema in lista_temas:
        print({tema})

"""_-------------------------------------------------------------------------------------------------------

PEGANDO O NOME DO EVENTO QUE FOI DIGITADO
_-------------------------------------------------------------------------------------------------------
"""