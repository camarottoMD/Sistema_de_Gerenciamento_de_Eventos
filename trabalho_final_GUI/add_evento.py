from datetime import datetime
from tkinter import *
from tkinter import ttk #utiliza widgets mais modernos

eventos = {}


def entry_evento(test_mode=True):
    add_janela = Toplevel()
    add_janela.title('Novo Evento')


    nome_var = StringVar()
    data_var = StringVar()
    tema_var = StringVar()

    Label(add_janela, text="Digite o nome do evento: ").grid(column=0, row=0)
    nome_entry = Entry(add_janela, textvariable=nome_var)
    nome_entry.grid(
        column=1, row=0
    )  # quando a variavel recebe .gri ela retorna none, então tem que fazer separado

    Label(add_janela, text="Digite a data do evento: ").grid(column=0, row=2)
    data_entry = Entry(add_janela, textvariable=data_var)
    data_entry.grid(
        column=1, row=2
    )  # quando a variavel recebe .gri ela retorna none, então tem que fazer separado

    Label(add_janela, text="Digite o tema do evento: ").grid(column=0, row=4)
    tema_entry = Entry(add_janela, textvariable=tema_var)
    tema_entry.grid(
        column=1, row=4
    )  # quando a variavel recebe .gri ela retorna none, então tem que fazer separado

    def salvar_evento():
        nome = nome_var.get()
        data = data_var.get()
        tema = tema_var.get()
        nome, data, tema = tratamento_var(nome, data, tema)
        adicionar_evento(nome, data, tema)
        add_janela.destroy()
    botao_cria = Button(add_janela, text="Adicionar evento", command=salvar_evento)
    botao_cria.grid(column=0, row=6)

        # --- Preenchimento automático para testes ---
    if test_mode:
        nome_var.set("Evento Teste")
        data_var.set("14/06/2025")
        tema_var.set("Teste Automático")
        # Chama o salvar_evento automaticamente após 1 segundo
        add_janela.after(1000, salvar_evento)

    return add_janela, nome_entry, data_var, tema_var


def tratamento_var(nome, data, tema):
    nome = nome.strip().title()
    tema = tema.strip().title()
    data = datetime.strptime(data, "%d/%m/%Y")
    return nome, data, tema

def adicionar_evento(nome, data, tema):
    eventos[nome] = {"data": data, "tema": tema}