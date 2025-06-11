from datetime import datetime
from tkinter import *

eventos = {}

def entry_evento():
    add_janela = Toplevel()
    
    nome_var = StringVar()
    data_var = StringVar() #todas definidas como variavel de str
    tema_var = StringVar()
    
    Label(add_janela, text="Digite o nome do evento: ").grid(column=0, row=0)
    nome_entry = Entry(add_janela, textvariable=nome_var).grid(column=1, row=0)
    
    Label(add_janela, text="Digite a data do evento: ").grid(column=0, row=1)
    data_entry = Entry(add_janela, textvariable=data_var).grid(column=1, row=1)
    
    Label(add_janela, text="Digite o tema do evento: ").grid(column=0, row=2)
    tema_entry = Entry(add_janela, datetime=tema_var).grid(column=1, row=2)


def salvar_evento():
    nome = nome_var.get() #get() captura o valor de nome_var
    data = data_var.get()
    tema = tema_var.get()
    print(f"Nome: {nome}, Data: {data}, Tema: {tema}")
    botao_addEvento = Button(add_janela, text='Adicionar evento', command=adicionar_evento).grid(column=0, row=3)#não pode colocar (), se naõ vou executar direto
    
    return add_janela, nome_entry, data_var, tema_var


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
    
    tema = tema_entry.strip().title()
    data = datetime.strptime(
        data_entry,
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