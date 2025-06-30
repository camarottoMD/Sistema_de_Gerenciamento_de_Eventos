from time import sleep
import uuid
from func_evento import *

participantes = dict() # == participante = {}

def adicionar_participante(nome_evento, test_mode=True):
    if test_mode:
        nome_user_input = "Matheus"
        id_user = uuid.uuid4()
        email_input = "user@email.com"
        prefs_input = "Gosto de IA, culinaria e Anime"

        print(f"Preenchimento automático: {nome_user_input}, {id_user}, {email_input}, {prefs_input}")
        sleep(3)
    else:
        #talvez adicionar um botao para voltar campo
        nome_user_input = input("Digite o seu nome completo: ")
        id_user = uuid.uuid4()
        email_input = input("Digite o seu email: ")
        prefs_input = input("Digite suas preferencias sobre temas de eventos: ")

    nome_user = (
        nome_user_input.strip().title()
    )

    if nome_user in participantes:
        print(f"O participante {nome_user}, já está participando deste evento.")
    else:
        #fazer um tratamento pra reconhecer que é um email normal mesmo, talvez com biblioteca
        email = email_input

        prefs = prefs_input.strip().title()
        participantes[id_user] = {
            "nome": nome_user,
            "email": email,
            "prefs": prefs,
            "eventos_inscrito": []
        }
        participantes[id_user]["eventos_inscrito"].append(nome_evento)

        eventos[nome_evento]["participantes"].append(participantes[id_user]['nome'])
        #fazer ele puxar os dados e jogar dentro do dicionario, porem quero fazer uma visualizacao mais botina - eventos[nome_evento]["participantes"].append(participantes[id_user].values())

        #tava fazendo o tratamento disso como dict, e era pra tratar como dicionario
        
        """_summary_
        preciso linkar os eventos com os participantes e vice versa, preciso mostrar quais eventos o participante esta inscrito
        
        Explicacao de como adicionar elementos em dicts
        Para adicionar um novo campo: dicionario["nova_chave"] = valor
        Para adicionar em uma lista dentro do dicionário: dicionario["chave_lista"].append(valor)
        Nunca sobrescreva o dicionário inteiro se quiser apenas adicionar um elemento!
        """

def buscarParticipante(nome_evento):
    while True:
        nomeParticipante = input("\nInsira o nome de um usuario: ").strip().title()
        if nomeParticipante in participantes:
            break
        else:
            print(f"\nO usuario {nomeParticipante} não existe! Insira novamente.")

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

def achar_id_usuario():
    nomeParticipante = input("\nInsira o nome do usuário que deseja editar: ").strip().title()
    # Procura o id do participante pelo nome
    for id_user, dados in participantes.items():
        if dados["nome"] == nomeParticipante:
            return id_user

def excluirParticipante():
    id_remove = achar_id_usuario()

    if id_remove:
        # Remove o participante de todos os eventos em que está inscrito
        for evento in eventos.values():
            if "participantes" in evento and id_remove in evento["participantes"]:
                evento["participantes"].remove(id_remove)
        # Remove o participante do dicionário de participantes
        del participantes[id_remove]
        print(f"Participante {nomeParticipante} removido do sistema e de todos os eventos.")
    else:
        print(f"O participante {nomeParticipante} não foi encontrado.")

def excluirParticipanteNoEvento(nome_evento):
    id_remove = achar_id_usuario()

    if id_remove and id_remove in eventos[nome_evento]["participantes"]:
        eventos[nome_evento]["participantes"].remove(id_remove)
        print(f"Participante {nomeParticipante} removido do evento '{nome_evento}'.")
    else:
        print(f"O participante {nomeParticipante} não está inscrito neste evento.")


def editarInfosParticipante():
    id_editar = achar_id_usuario()

    if not id_editar:
        print("Participante não encontrado.")
        return

    print("1 - Editar Nome do Participante")
    print("2 - Editar Email do Participante")
    print("3 - Editar Preferencias do Participante")
    opEdit = input('Insira uma das opcoes acima: ')

    match opEdit:
        case "1":
            novo_nome = input("Digite o novo nome: ").strip().title()
            participantes[id_editar]["nome"] = novo_nome
            print("Nome alterado com sucesso.")
        case "2": 
            novo_email = input("Digite o novo email: ").strip()
            participantes[id_editar]["email"] = novo_email
            print("Email alterado com sucesso.")
        case "3": 
            novas_prefs = input("Digite as novas preferências: ").strip().title()
            participantes[id_editar]["prefs"] = novas_prefs
            print("Preferências alteradas com sucesso.")