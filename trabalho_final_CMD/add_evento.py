from datetime import datetime

eventos = {}


def adicionar_evento(test_mode=True):
    if test_mode:
        nome_input = "Evento Teste"
        data_input = "15/06/2025"
        tema_input = "Teste Automático"
        hora_input = "19:30"

        print(f"Preenchimento automático: {nome_input}, {data_input}, {tema_input}")
    else:
        nome_input = input("Digite o nome do evento: ")
        data_input = input("Digite a data do evento (dd/mm/aaaa): ")
        hora_input = input("Digite a hora do evento (hh:mm): ")
        tema_input = input("Digite o tema do evento: ")
    """
    verificação de nome duplicado e exibição de mensagem
    """
    for nome in eventos.keys():
        if nome_input == nome:
            print(
                f"O evento '{nome}' não pode ser registrado! O nome '{nome}', já esta sendo utilizado"
            )
        else:
            """_summary_
            verificação de nome duplicado para print do erro, pois o ID dos eventos são os nomes, e o dicionario
            ja nao permite keys iguais
            """

            nome_evento = (
                nome_input.strip().title()
            )  # Remove espaços no fim e começo e coloca a primeira letra em maiúsculo

            # fazer tratamento de id de evento, porem se for fazer com banco ta de boa

            data = datetime.strptime(
                data_input,
                "%d/%m/%Y",  # -> so a aceita nesse formato
            )  # strptime = string → data / strftime = data → string    #   $d->dia em numeral     %m-> mes em numeral     %Y-> ano completo em numeral

            hora = datetime.strptime(hora_input, "%H:%M")

            tema = tema_input.strip().title()

            eventos[nome_evento] = {
                "data": data,
                "hora": hora,
                "tema": tema,
                "participantes": [],
            }  # -> == eventos = {nome_evento: {"data": data, "tema": tema, "participantes": []}} isso seria a criacao do dic fora do def
