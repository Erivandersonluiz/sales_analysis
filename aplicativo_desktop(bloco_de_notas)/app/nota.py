import tkinter as tk
from tkinter import filedialog, messagebox

class EditorNotas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Editor de Notas")
        self.geometry("600x400")

        # Área de texto
        self.texto_area = tk.Text(self)
        self.texto_area.pack(expand=True, fill=tk.BOTH)

        # Menu
        self.criar_menu()

    def criar_menu(self):
        menubar = tk.Menu(self)
        arquivo_menu = tk.Menu(menubar, tearoff=0)
        arquivo_menu.add_command(label="Abrir", command=self.abrir_arquivo)
        arquivo_menu.add_command(label="Salvar", command=self.salvar_arquivo)
        arquivo_menu.add_separator()
        arquivo_menu.add_command(label="Sair", command=self.quit)
        menubar.add_cascade(label="Arquivo", menu=arquivo_menu)
        self.config(menu=menubar)

    def abrir_arquivo(self):
        caminho = filedialog.askopenfilename(
            filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")]
        )
        if not caminho:
            return

        try:
            with open(caminho, "r", encoding="utf-8") as arquivo:
                texto = arquivo.read()
            self.texto_area.delete(1.0, tk.END)
            self.texto_area.insert(tk.END, texto)
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível abrir o arquivo:\n{e}")

    def salvar_arquivo(self):
        caminho = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")]
        )
        if not caminho:
            return

        try:
            texto = self.texto_area.get(1.0, tk.END)
            with open(caminho, "w", encoding="utf-8") as arquivo:
                arquivo.write(texto)
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível salvar o arquivo:\n{e}")

if __name__ == "__main__":
    app = EditorNotas()
    app.mainloop()