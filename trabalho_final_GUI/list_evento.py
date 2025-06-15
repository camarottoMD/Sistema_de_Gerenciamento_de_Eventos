from add_evento import *
from tkinter import * #traz todas as tags que precisamos
from tkinter import ttk #utiliza widgets mais modernos

def listar_eventos():
    
    #POSSO UTILIZAR ENTRY NO TREE PRA PODER EDITAR AS INFOS QUE PODEM SER EDITAVEIS DEPOIS
    
    """_summary_
    Você precisa acessar assim porque cada valor do dicionário principal (eventos) é outro dicionário com os detalhes do evento.
Esse padrão facilita organizar e acessar as informações de cada evento de forma clara e estruturada.
    """
    #-----------------------------------------------------------------------------------------------------------------------------------------   
    for evento_nome, evento_infos in eventos.items(): #.items, recebe chave e values, no caso o evento_nome vai ser key e evento_infos vai ser value
        print(f"Nome: {evento_nome}")
        print(f"Data: {evento_infos['data']}")
        print(f"Tema: {evento_infos['tema']}")
        #print(f"Participantes: {evento_infos['participantes']}")
        
    #-----------------------------------------------------------------------------------------------------------------------------------------        

    list_janela = Toplevel()
    list_janela.title("Lista de Eventos")

    tree = ttk.Treeview(list_janela, columns=("Tema", "Data", "Participantes")) # cria a tabela dentro da janela e define as colunas
    tree.heading("#0", text="Nome")  # Cabeçalho da coluna "Row"
    tree.heading("Tema", text= nome)
    tree.heading("Data", text="Coluna 2")
    tree.heading("Participantes", text="Coluna 3")

    tree.insert("", "end", text="Linha 1", values=("Valor 1", "Valor 2", "Valor 3"))
    tree.insert("", "end", text="Linha 2", values=("Valor 4", "Valor 5", "Valor 6")) #fazer um laço de repetição pra voltar
    tree.insert("", "end", text="Linha 3", values=("Valor 7", "Valor 8", "Valor 9"))

    tree.pack(expand=True, fill="both")  # Posiciona a Treeview na tela
    
    botao_exit_list = ttk.Button(list_janela,  text="Sair", command=list_janela.destroy)
    botao_exit_list.grid(column=0, row=4)
