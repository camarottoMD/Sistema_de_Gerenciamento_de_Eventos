from list_evento import *   
from add_evento import *
from tkinter import *
from tkinter import ttk

window = Tk()

window.title('Sistema de Gerenciamento de Eventos')

#menu = ttk.Frame(window, padding=50)

texto = Label(window, text="Clique nos seguintes botões")
texto.grid(column=0, row=0)

#sempre passar qual janela como parametro
botao_add = Button(window, text='Adicionar evento', command=entry_evento).grid(column=0, row=1)#não pode colocar (), se naõ vou executar direto
botao_list = Button(window, text='Listar Eventos', command=listar_eventos).grid(column=0, row=2)
botao_exit = Button(window, text='Encerrar programa', command=exit).grid(column=0, row=3)


def abrir_tela_adicionar():
    add_evento_janela, entrada = entry_evento()
    entrada.insert(0, "Texto padrão")




'''texto.grid(row=0, column=0)'''
'''ttk.Button(menu, text="1 - Listagem de Eventos", command=menu.destroy).grid(column=1, row=0)
ttk.Button(menu, text="2 - Adicionar Evento", command=menu.destroy).grid(column=1, row=1)
ttk.Button(menu, text="3 - Sair", command=menu.destroy).grid(column=1, row=2)
'''

'''def menu():
    print("1 - Listagem de Eventos")
    print("2 - Adicionar Evento")
    print("3 - Sair")
    opcaoMenu()
'''

'''def opcaoMenu():
    escolhaOp = int(input("Selecione um número correspondente as opções acima: "))
    if escolhaOp == 1:
        listar_eventos()
    elif escolhaOp == 2:
        adicionar_evento()
    elif escolhaOp == 3:
        exit()'''

'''
while True:
    menu() #usar para terminal
    '''
window.mainloop()