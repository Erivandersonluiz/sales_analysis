import tkinter as tk
from tkinter import filedialog, messagebox

class MinhaJanela(tk.Tk):
    def __init__(self):         
        super().__init__()
        self.title("Minha Janela")
        self.geometry("400x300")

        # Criar menu
        self.criar_menu()

    def criar_menu(self):
        menubar = tk.Menu(self)
        arquivo_menu = tk.Menu(menubar, tearoff=0)
        arquivo_menu.add_command(label="Abrir", command=self.abrir)
        arquivo_menu.add_command(label="Salvar", command=self.salvar)
        menubar.add_cascade(label="Arquivo", menu=arquivo_menu)
        self.config(menu=menubar)

    def abrir(self):
        caminho = filedialog.askopenfilename(
            filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")]
        )
        if caminho:
            messagebox.showinfo("Arquivo selecionado", f"Arquivo: {caminho}")

    def salvar(self):
        caminho = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")]
        )
        if caminho:
            messagebox.showinfo("Salvar em", f"Salvar em: {caminho}")

if __name__ == "__main__":
    app = MinhaJanela()
    app.mainloop()