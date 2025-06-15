from datetime import datetime

eventos = {}

def adicionar_evento(test_mode = False):

    if test_mode:
        nome_input = "Evento Teste"
        data_input = "15/06/2025"
        tema_input = "Teste Automático"
        print(f"Preenchimento automático: {nome_input}, {data_input}, {tema_input}")
    else: 
        nome_input= input("Digite o nome do evento: ")
        data_input = input("Digite a data do evento (dd/mm/aaaa): ")
        tema_input = input("Digite o tema do evento: ")


    nome_evento = (
        nome_input.strip().title()
    )  # Remove espaços no fim e começo e coloca a primeira letra em maiúsculo

    # fazer tratamento de id de evento, porem se for fazer com banco ta de boa
    
    data = datetime.strptime(
        data_input,
        "%d/%m/%Y" #-> so a aceita nesse formato
    )  # strptime = string → data / strftime = data → string    #   $d->dia em numeral     %m-> mes em numeral     %Y-> ano completo em numeral

    tema = tema_input.strip().title()

    eventos[nome_evento] = {
        "data": data,
        "tema": tema,
        "participantes": [],
    }  # -> == eventos = {nome_evento: {"data": data, "tema": tema, "participantes": []}} isso seria a criacao do dic fora do def

