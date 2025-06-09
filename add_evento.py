from datetime import datetime

eventos = {}

def adicionar_evento():
    nome_evento = input("Digite o nome do evento: ")
    data = input("Digite a data do evento (dd/mm/aaaa): ")
    tema = input("Digite o tema do evento: ")

    nome_evento = (
        nome_evento.strip().title()
    )  # Remove espaços no fim e começo e coloca a primeira letra em maiúsculo

    #id de evento
    
    tema = tema.strip().title()
    data = datetime.strptime(
        data,
        "%d/%m/%Y" #-> so a aceita nesse formato
    )  # strptime = string → data / strftime = data → string    #   $d->dia em numeral     %m-> mes em numeral     %Y-> ano completo em numeral

    eventos[nome_evento] = {
        "data": data,
        "tema": tema,
        "participantes": [],
    }  # -> == eventos = {nome_evento: {"data": data, "tema": tema, "participantes": []}} isso seria a criacao do dic fora do def
    print("aqui")
    print(eventos)
