from cad_user import participantes
from add_evento import eventos

def buscarParticipante(nome_evento):
    while True:
        nomeParticipante = input("Insira o nome de um usuario: ")
        if nomeParticipante in participantes:
            break
        else:
            print(f"O usuario {nomeParticipante} não existe! Insira novamente.")

    if nomeParticipante in eventos[nome_evento]['participantes']:
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

def excluirParticipante():
    pass
def excluirUser():
    pass
def editarInfosUser():
    pass