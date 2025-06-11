from add_evento import *
from tkinter import * #traz todas as tags que precisamos
from tkinter import ttk #utiliza widgets mais modernos

def listar_eventos():
    list_janela = Toplevel()
    
    #POSSO UTILIZAR ENTRY NO TREE PRA PODER EDITAR AS INFOS QUE PODEM SER EDITAVEIS DEPOIS
    
    list_janela.title("Lista de Eventos")

    tree = ttk.Treeview(list_janela, columns=("Column1", "Column2", "Column3")) # cria a tabela dentro da janela e define as colunas
    tree.heading("#0", text="Row")  # Cabeçalho da coluna "Row"
    tree.heading("Column1", text=eventos[nome])
    tree.heading("Column2", text="Coluna 2")
    tree.heading("Column3", text="Coluna 3")

    tree.insert("", "end", text="Linha 1", values=("Valor 1", "Valor 2", "Valor 3"))
    tree.insert("", "end", text="Linha 2", values=("Valor 4", "Valor 5", "Valor 6")) #fazer um laço de repetição pra voltar
    tree.insert("", "end", text="Linha 3", values=("Valor 7", "Valor 8", "Valor 9"))

    tree.pack(expand=True, fill="both")  # Posiciona a Treeview na tela
    
    botao_exit_list = ttk.Button(list_janela,  text="Sair", command=list_janela.destroy)
    botao_exit_list.grid(column=0, row=4)
