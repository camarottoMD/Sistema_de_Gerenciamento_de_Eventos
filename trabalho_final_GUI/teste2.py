import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.title("Tabela com Treeview")

tree = ttk.Treeview(root, columns=("Column1", "Column2", "Column3"))
tree.heading("#0", text="Row")  # Cabeçalho da coluna "Row"
tree.heading("Column1", text="Coluna 1")
tree.heading("Column2", text="Coluna 2")
tree.heading("Column3", text="Coluna 3")

tree.insert("", "end", text="Linha 1", values=("Valor 1", "Valor 2", "Valor 3"))
tree.insert("", "end", text="Linha 2", values=("Valor 4", "Valor 5", "Valor 6"))
tree.insert("", "end", text="Linha 3", values=("Valor 7", "Valor 8", "Valor 9"))

tree.pack(expand=True, fill="both")  # Posiciona a Treeview na tela

root.mainloop()