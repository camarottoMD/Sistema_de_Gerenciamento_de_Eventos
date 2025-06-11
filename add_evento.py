from datetime import datetime
from tkinter import *

eventos = {}

def entry_evento():
    add_evento_janela = Toplevel()
    nome_evento = Entry(add_evento_janela, textvariable="Digite o nome do evento: ").grid(column=0, row=1)
    data_evento = Entry(add_evento_janela, textvariable="Digite a data do evento: ").grid(column=0, row=2)
    tema_evento = Entry(add_evento_janela, datetime="Digite o tema do evento: ").grid(column=0, row=3)
    
    botao = Button(add_evento_janela, text='Adicionar evento', command=adicionar_evento)#não pode colocar (), se naõ vou executar direto
    return add_evento_janela, nome_evento, data_evento, tema_evento

def adicionar_evento():
    
    """
    nome_evento = input("Digite o nome do evento: ")
    data = input("Digite a data do evento (dd/mm/aaaa): ")
    tema = input("Digite o tema do evento: ")
    """

    nome_evento = (
        nome_evento.strip().title()
    )  # Remove espaços no fim e começo e coloca a primeira letra em maiúsculo

    # fazer tratamento de id de evento, porem se for fazer com banco ta de boa
    
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

def criar_evento():
    ...

def del_evento():
    ...
    
add_evento_janela.mainloop()