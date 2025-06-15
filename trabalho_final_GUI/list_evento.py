from add_evento import *
from tkinter import * #traz todas as tags que precisamos
from tkinter import ttk #utiliza widgets mais modernos

"""_summary_
    Treeview funciona como uma lista hierarquica para GUI, suportando tambem dados nao hierarquicos.
    Pode ser utilizado como widget de tabela.
    O primeiro parametro a ser passado e o item pai, ou se nao uma str vazia, mostrando que nao existe antecessor
    O segudo parametro e o indice de onde aquele elemento vai ser adicionado. Se colocado end os itens vao sendo adicionados um apos o outro
"""

def listar_eventos():
    
    """_summary_
    POSSO UTILIZAR ENTRY NO TREE PRA PODER EDITAR AS INFOS QUE PODEM SER EDITAVEIS DEPOIS
    

    Você precisa acessar assim porque cada valor do dicionário principal (eventos) é outro dicionário com os detalhes do evento.
    Esse padrão facilita organizar e acessar as informações de cada evento de forma clara e estruturada.
    """    

    list_janela = Toplevel()
    list_janela.title("Lista de Eventos")

    tabela = ttk.Treeview(list_janela, columns=("tema", "data", "participantes")) # cria a tabela dentro da janela e define as colunas
    tabela.heading("#0", text="Nome do Evento")  # Cabeçalho da coluna "Row"
    tabela.heading("tema", text= 'Tema')
    tabela.heading("data", text="Data")
    tabela.heading("participantes", text="Participantes")

    for evento_nome, evento_infos in eventos.items(): #.items, recebe chave e values, no caso o evento_nome vai ser key e evento_infos vai ser value
        tabela.insert("", "end", text=evento_nome, values=(evento_infos['data'], evento_infos['tema'])) #evento_infos['participantes'])) #fazer um laço de repetição pra voltar, aqui que vai ficar o valor das linhas

    tabela.pack(expand=True, fill="both")  # Posiciona a Treeview na tela, fill faz com que ele expanda tanto para vertical quanto para horizontal, expand faz com que ele cresça quando a pagina for aumentada ou diminuida
    
    botao_exit_list = ttk.Button(list_janela,  text="Sair", command=list_janela.destroy)
    botao_exit_list.grid(column=0, row=4)
