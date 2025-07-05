import uuid
import os
from func_evento import *

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

participantes = dict() 
participantes = dict()

def adicionar_participante(nome_evento):
    """
    adiciona um novo participante ao sistema e o inscreve em um evento.
    solicita nome, email e preferências do usuário, faz validações e atualiza os dicionários globais.
    """
    while True:
        nome_user_input = input("Digite o seu nome completo: ").strip()
        if not nome_user_input:
            print("Nome não pode ser vazio.")
            continue
        break
    id_user = uuid.uuid4()
    while True:
        email_input = input("Digite o seu email: ").strip().lower()
        if not email_input or "@" not in email_input or "." not in email_input:
            print("Email inválido. Por favor, insira um email válido.")
            continue
        if any(p.get("email", "").lower() == email_input for p in participantes.values()):
            print("Este email já está cadastrado. Por favor, insira outro email.")
        else:
            break
    prefs_input = input("Digite suas preferencias sobre temas de eventos: ")

    nome_user = nome_user_input.strip().title()

    if nome_user in [p.get("nome") for p in participantes.values()]:
        print(f"O participante {nome_user}, já está participando deste evento.")
    else:
        email = email_input
        prefs = prefs_input.strip().title()
        participantes[id_user] = {
            "nome": nome_user,
            "email": email,
            "prefs": prefs,
            "eventos_inscrito": []
        }
        participantes[id_user]["eventos_inscrito"].append(nome_evento)
        # adiciona o participante ao evento, se o evento existir
        if nome_evento in eventos:
            eventos[nome_evento]["participantes"].append(participantes[id_user].get('nome'))
        else:
            print(f"Evento '{nome_evento}' não encontrado para adicionar participante.")

def buscarParticipante(nome_evento=None):
    """
    busca e exibe informações detalhadas de um participante pelo nome.
    se nome_evento for fornecido, verifica se o participante está inscrito no evento.
    """
    while True:
        nomeParticipante = input("\nInsira o nome de um usuário: ").strip().title()
        if not nomeParticipante:
            print("Nome não pode ser vazio.")
            continue
        id_encontrado = None
        for id_user, dados in participantes.items():
            if dados.get("nome") == nomeParticipante:
                id_encontrado = id_user
                break
        if not id_encontrado:
            print(f"\nO usuário {nomeParticipante} não existe! Insira novamente.")
            return
        # se nome_evento foi passado, verifica se o participante está inscrito no evento
        if nome_evento:
            if nomeParticipante not in eventos.get(nome_evento, {}).get('participantes', []):
                print(f"O participante {nomeParticipante} não está inscrito no evento '{nome_evento}'.")
                return
        print("\n" + "="*30)
        print(f"INFORMAÇÕES DO PARTICIPANTE")
        print("-"*30)
        print(f"Nome: {participantes.get(id_encontrado, {}).get('nome')}")
        print(f"Email: {participantes.get(id_encontrado, {}).get('email')}")
        print(f"Preferências: {participantes.get(id_encontrado, {}).get('prefs')}")
        print(f"Eventos inscritos:")
        for evento in participantes.get(id_encontrado, {}).get('eventos_inscrito', []):
            print(f"{evento}")
        print("="*30)
        # exibe os eventos em que o participante está inscrito
        print("\nEventos detalhados:")
        for nome, info in eventos.items():
            if nomeParticipante in info.get('participantes', []):
                print("-" * 20)
                print(f"Evento: {nome}")
                print(f"  Data: {info.get('data').strftime('%d/%m/%Y') if info.get('data') else 'N/A'}")
                print(f"  Horário: {info.get('hora').strftime('%H:%M') if info.get('hora') else 'N/A'}")
                print(f"  Tema: {info.get('tema', 'N/A')}")
                print(f"  Participantes: {info.get('participantes', [])}")
        print("-" * 20)
        break

def achar_id_usuario():
    """
    busca o ID de um participante pelo email informado pelo user e 
    retorna o ID se encontrado, ou None caso não encontre
    """
    while True:
        emailParticipante = input("\nInsira o email do usuário que deseja editar: ").strip().lower()
        if not emailParticipante:
            print("Email não pode ser vazio.")
            continue
        for id_user, dados in participantes.items():
            if dados.get("email", "").lower() == emailParticipante:
                return id_user
        print("Participante não encontrado.")
        return None

def excluirParticipante():
    """
    remove um participante do sistema e de todos os eventos em que está inscrito.
    """
    id_remove = achar_id_usuario()

    if id_remove:
        # remove o participante de todos os eventos em que está inscrito
        for evento in eventos.values():
            if "participantes" in evento and id_remove in evento.get("participantes", []):
                evento.get("participantes", []).remove(id_remove)
        # remove o participante do dicionário de participantes
        del participantes[id_remove]
        print(f"Participante removido do sistema e de todos os eventos.")
    else:
        print(f"O participante não foi encontrado.")

def excluirParticipanteNoEvento(nome_evento):
    id_remove = achar_id_usuario()

    if id_remove and id_remove in eventos.get(nome_evento, {}).get("participantes", []):
        eventos.get(nome_evento, {}).get("participantes", []).remove(id_remove)
        print(f"Participante removido do evento '{nome_evento}'.")
    else:
        print(f"O participante não está inscrito neste evento.")


def editarInfosParticipante():
    """
    permite editar nome, email ou preferências de um participante já cadastrado.
    """
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
            if not novo_nome:
                print("Nome não pode ser vazio.")
            else:
                participantes.get(id_editar, {})["nome"] = novo_nome
                print("Nome alterado com sucesso.")
        case "2": 
            while True:
                novo_email = input("Digite o novo email: ").strip()
                if not novo_email or "@" not in novo_email or "." not in novo_email:
                    print("Email inválido. Por favor, insira um email válido.")
                    continue
                participantes.get(id_editar, {})["email"] = novo_email
                print("Email alterado com sucesso.")
                break
        case "3": 
            novas_prefs = input("Digite as novas preferências: ").strip().title()
            participantes.get(id_editar, {})["prefs"] = novas_prefs
            print("Preferências alteradas com sucesso.")

def listar_eventos_por_tema():
    tema_busca = input("Digite o tema para listar os eventos: ").strip().title()
    eventos_do_tema = list(filter(lambda e: e.get('tema') == tema_busca, eventos.values()))
    if eventos_do_tema:
        print(f"\nEventos com o tema '{tema_busca}':")
        for evento in eventos_do_tema:
            print("-" * 20)
            print(f"Evento: {evento.get('tema')}")
            print(f"  Data: {evento.get('data').strftime('%d/%m/%Y') if evento.get('data') else 'N/A'}")
            print(f"  Horário: {evento.get('hora').strftime('%H:%M') if evento.get('hora') else 'N/A'}")
            print(f"  Participantes: {evento.get('participantes', [])}")
    else:
        print(f"Nenhum evento encontrado com o tema '{tema_busca}'.")