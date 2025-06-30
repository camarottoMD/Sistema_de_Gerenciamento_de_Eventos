#JUNTANDO AS FUNC DE EVENTO 

from datetime import datetime

# Variaveis globais


# Memória
eventos = dict()
lista_temas = list()

def adicionar_evento():

    while True:
        nome_input = input("Digite o nome do evento: ")

        nome_evento = (
        nome_input.strip().title()
    )  # Remove espaços no fim e começo e coloca a primeira letra em maiúsculo

        if nome_evento in eventos:
            print(
                f"O evento '{nome_evento}' não pode ser registrado! O nome '{nome_evento}', já esta sendo utilizado"
            )
        else:
            break
        
    while True:
        try:
            data_input = input("Digite a data do evento (dd/mm/aaaa): ")
            data = datetime.strptime(
                data_input,
                "%d/%m/%Y",  # -> so a aceita nesse formato
            )  # strptime = string → data / strftime = data → string    #   $d->dia em numeral     %m-> mes em numeral     %Y-> ano completo em numeral
            break
        except ValueError:
            print("Data com valor/formato incorreto! Adicione novamente")
    while True:
        try:
            hora_input = input("Digite a hora do evento (hh:mm): ")
            hora = datetime.strptime(hora_input, "%H:%M")
            break
        except ValueError:
            print("Data com valor/formato incorreto! Adicione novamente")

    tema_input = input("Digite o tema do evento: ")
    tema_input = tema_input.strip().title()
    if tema_input in eventos:
        pass
    else:
        lista_temas.append(tema_input)

    eventos[nome_evento] = {
        "data": data,
        "hora": hora,   #desta maneira eu não preciso percorrer as listas para remover ou editar qualquer tipo de evento
        "tema": tema_input,
        "participantes": [],
    }  # -> == eventos = {nome_evento: {"data": data, "tema": tema, "participantes": []}} isso seria a criacao do dic fora do def

    #tabelaLigacao =
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

    
def listar_temas():
    print("-" * 20)
    for tema in lista_temas:
        print({tema})

def remover_evento():
    pass

def editar_evento():
    while True:
        evento_a_ser_editado = input("Digite o nome do evento a ser editado: ")
        if evento_a_ser_editado in eventos:
            print("1 - Alterar nome\n2 - Alterar data\n3 - Alterar tema\n4 - Alterar horário\n")
            opc_editar = input("Digite a opção a ser editada (0 para sair): ")

            match opc_editar:
                case "0":
                    break
                case "1":
                    while True:
                        if evento_a_ser_editado in eventos:
                                
                            while True:
                                nome_editado = input("Digite o Novo Nome para o evento: ")
                                if nome_editado in eventos:
                                    print("Evento com nome ({nome_editado}) já existe em Eventos!")
                                else:
                                    eventos[nome_editado] = eventos[evento_a_ser_editado]
                                    del eventos[evento_a_ser_editado]
                                    print(nome_editado)
                                    break
                        break
                case "2":
                    nova_data = input("Digite a nova data (dd/mm/aaaa): ")
                    try:
                        eventos[evento_a_ser_editado]["data"] = datetime.strptime(nova_data, "%d/%m/%Y")
                        print("Data alterada com sucesso.")
                    except Exception:
                        print("Data inválida!")
                    break
                case "3":
                    novo_tema = input("Digite o novo tema: ").strip().title()
                    eventos[evento_a_ser_editado]["tema"] = novo_tema
                    print("Tema alterado com sucesso.")
                    break
                case "4":
                    novo_horario = input("Digite o novo horário (hh:mm): ")
                    try:
                        eventos[evento_a_ser_editado]["hora"] = datetime.strptime(novo_horario, "%H:%M")
                        print("Horário alterado com sucesso.")
                    except Exception:
                        print("Horário inválido!")
                    break
                case _:
                    print("Opção inválida.")
        else:
            print("Evento não encontrado.")