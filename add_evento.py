from datetime import datetime
name_evento = input("Digite o nome do evento: ")
data_str = input("Digite a data do evento (dd/mm/aaaa): ")
tema = input("Digite o tema do evento: ")

def adicionar_evento(name_evento, data_str, tema):
    name_evento = (
        name_evento.strip().title()
    )  # Remove espaços no fim e começo e coloca a primeira letra em maiúsculo

    global data
    data = datetime.strptime(data_str, "%d/%m/%Y")    #strptime = string → data / strftime = data → string    #   $d->dia em numeral     %m-> mes em numeral     %Y-> ano completo em numeral

    eventos[name_evento][name_evento] = name_evento
    eventos[name_evento]["data"] = data
    eventos[name_evento]["tema"] = tema
    # eventos[name_evento]["participantes"] = []


eventos = {name_evento: {"data": data, "tema": tema, "participantes": []}}
print(eventos)
