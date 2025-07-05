from datetime import datetime
import os

# variaveis globais
lista_temas = list()
eventos = dict()
participantes = dict()

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def adicionar_evento():
    """
    adiciona um novo evento ao sistema.
    solicita nome, data, horário e tema, faz validações e atualiza o dicionário global de eventos.
    """
    limpar_tela()

    while True:
        nome_input = input("Digite o nome do evento: ").strip()
        if not nome_input:
            print("Nome do evento não pode ser vazio!")
            continue
        nome_evento = nome_input.title()
        if nome_evento in eventos:
            print(
                f"O evento '{nome_evento}' não pode ser registrado! O nome '{nome_evento}', já está sendo utilizado"
            )
        else:
            break
        
    while True:
        try:
            data_input = input("Digite a data do evento (dd/mm/aaaa): ").strip()
            if not data_input:
                print("Data não pode ser vazia!")
                continue
            data = datetime.strptime(
                data_input,
                "%d/%m/%Y",
            )
            break
        except ValueError:
            print("Data com valor/formato incorreto! Adicione novamente")
    while True:
        try:
            hora_input = input("Digite a hora do evento (hh:mm): ").strip()
            if not hora_input:
                print("Horário não pode ser vazio!")
                continue
            hora = datetime.strptime(hora_input, "%H:%M")
            break
        except ValueError:
            print("Horário com valor/formato incorreto! Adicione novamente")

    while True:
        tema_input = input("Digite o tema do evento: ").strip()
        if not tema_input:
            print("Tema não pode ser vazio!")
            continue
        tema_input = tema_input.title()
        if tema_input not in lista_temas:
            lista_temas.append(tema_input)
        break

    eventos[nome_evento] = {
        "data": data,
        "hora": hora,  
        "tema": tema_input,
        "participantes": [],
    }

def listar_eventos():
    """
    exibe todos os eventos cadastrados com seus detalhes (nome, data, horário, tema e participantes).
    """
    limpar_tela()
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

    
def listar_temas():
    """
    lista todos os temas de eventos cadastrados no sistema.
    """
    print("-" * 20)
    for tema in lista_temas:
        print({tema})
    input("Pressione Enter para continuar...")

def remover_evento():
    """
    remove um evento do sistema e atualiza os participantes inscritos nesse evento.
    """
    limpar_tela()
    from func_user import participantes
    while True:
        nome_evento = input("Digite o nome do evento a ser removido: ").strip().title()
        if not nome_evento:
            print("Nome do evento não pode ser vazio!")
            continue
        if nome_evento in eventos:
            # remove o evento da lista de eventos inscritos de cada participante
            for id_user, dados in list(participantes.items()):
                if 'eventos_inscrito' in dados and nome_evento in dados['eventos_inscrito']:
                    dados['eventos_inscrito'].remove(nome_evento)
            # remove o evento do dicionário de eventos
            del eventos[nome_evento]
            print(f"Evento '{nome_evento}' removido com sucesso!")
            break
        else:
            print(f"Evento '{nome_evento}' não encontrado.")
            break

def editar_evento():
    """
    edita nome, data, horário ou tema de um evento já cadastrado.
    """
    # limpar_tela()  # Removido
    evento_a_ser_editado = input("Digite o nome do evento a ser editado: ").strip().title()
    if not evento_a_ser_editado:
        print("Nome do evento não pode ser vazio!")
        return
    if evento_a_ser_editado in eventos:
        while True:
            print("1 - Alterar nome\n2 - Alterar data\n3 - Alterar horário\n4 - Alterar tema\n0 - Voltar\n")
            opc_editar = input("Digite a opção a ser editada (0 para sair): ").strip()
            if opc_editar == '0':
                break
            elif opc_editar == "1":
                while True:
                    nome_editado = input("Digite o Novo Nome para o evento: ").strip().title()
                    if not nome_editado:
                        print("Nome não pode ser vazio!")
                        continue
                    if nome_editado in eventos:
                        print(f"Evento com nome ({nome_editado}) já existe em Eventos!")
                    else:
                        eventos[nome_editado] = eventos[evento_a_ser_editado]
                        del eventos[evento_a_ser_editado]
                        print("Nome alterado com sucesso!")
                        break
            elif opc_editar == '2':
                nova_data = input("Digite a nova data (dd/mm/aaaa): ").strip()
                try:
                    if not nova_data:
                        print("Data não pode ser vazia!")
                        continue
                    eventos[evento_a_ser_editado]["data"] = datetime.strptime(nova_data, "%d/%m/%Y")
                    print("Data alterada com sucesso.")
                except Exception:
                    print("Data inválida!")
                break
            elif opc_editar == '3':
                novo_horario = input("Digite o novo horário (hh:mm): ").strip()
                try:
                    if not novo_horario:
                        print("Horário não pode ser vazio!")
                        continue
                    eventos[evento_a_ser_editado]["hora"] = datetime.strptime(novo_horario, "%H:%M")
                    print("Horário alterado com sucesso.")
                except Exception:
                    print("Horário inválido!")
                break
            elif opc_editar == '4':
                novo_tema = input("Digite o novo tema: ").strip().title()
                if not novo_tema:
                    print("Tema não pode ser vazio!")
                    continue
                eventos[evento_a_ser_editado]["tema"] = novo_tema
                print("Tema alterado com sucesso.")
                break
            else:
                print("Opção inválida.")
    else:
        print("Evento não encontrado.")