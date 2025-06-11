from list_evento import *   
from add_evento import *
from tkinter import *
from tkinter import ttk #utiliza widgets mais modernos


window = Tk()

window.geometry("600x400")
window.title('Sistema de Gerenciamento de Eventos')

texto = Label(window, text="Clique nos seguintes botões")
texto.grid(column=0, row=0)

#sempre passar qual janela como parametro
botao_add = Button(window, text='Adicionar evento', command=entry_evento)#não pode colocar (), se naõ vou executar direto
botao_add.grid(column=0, row=2)
botao_list = Button(window, text='Listar Eventos', command=listar_eventos)
botao_list.grid(column=0, row=4)
botao_exit = Button(window, text='Encerrar programa', command=exit)
botao_exit.grid(column=0, row=6)
    
window.mainloop()