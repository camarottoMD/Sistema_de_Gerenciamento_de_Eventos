from list_evento import *   
from add_evento import *
"""from tkinter import *
from tkinter import ttk"""

"""window = Tk()

window.title('Sistema de Gerenciamento de Eventos')"""

#menu = ttk.Frame(window, padding=50)
"""
texto = Label(window, text="Clique nos seguintes botões")
texto.grid(column=0, row=0)

#sempre passar qual janela como parametro
botao_add = Button(window, text='Adicionar evento', command=entry_evento).grid(column=0, row=1)#não pode colocar (), se naõ vou executar direto
botao_list = Button(window, text='Listar Eventos', command=listar_eventos).grid(column=0, row=2)
botao_exit = Button(window, text='Encerrar programa', command=exit).grid(column=0, row=3)"""

def menu():
    print("1 - Listagem de Eventos")
    print("2 - Adicionar Evento")
    print("3 - Sair")
    opcaoMenu()


def opcaoMenu():
    escolhaOp = int(input("Selecione um número correspondente as opções acima: "))
    if escolhaOp == 1:
        listar_eventos()
    elif escolhaOp == 2:
        adicionar_evento()
    elif escolhaOp == 3:
        exit()


while True:
    menu() #usar para terminal

#window.mainloop()