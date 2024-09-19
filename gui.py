import tkinter as tk
from tkinter import filedialog, messagebox
from lexer import analizar_archivo


class AnalizadorLexicoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Léxico")

        self.text_area = tk.Text(root, wrap="word")
        self.text_area.pack(expand=1, fill="both")

        self.menu = tk.Menu(root)
        root.config(menu=self.menu)

        file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Abrir", command=self.abrir_archivo)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=root.quit)

        self.resultado = tk.Text(root, wrap="word", state="disabled")
        self.resultado.pack(expand=1, fill="both")

    def abrir_archivo(self):
        archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
        if archivo:
            with open(archivo, "r") as file:
                contenido = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, contenido)
                self.analizar_contenido(contenido)

    def analizar_contenido(self, contenido):
        resultado = analizar_archivo(contenido)
        self.resultado.config(state="normal")
        self.resultado.delete(1.0, tk.END)
        for numero_linea, tokens in resultado:
            self.resultado.insert(tk.END, f"Línea {numero_linea}:\n")
            for token, tipo in tokens:
                self.resultado.insert(tk.END, f"  {token} -> {tipo}\n")
        self.resultado.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = AnalizadorLexicoApp(root)
    root.mainloop()
