import tkinter as tk
from tkinter import filedialog, messagebox
from lexer import analizar_archivo
from afd import RegexToAFD
from semantic_analyzer import analizar_semantica  # Importar el nuevo módulo

class AnalizadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Léxico y de Expresiones Regulares")
        self.root.geometry("800x600")
        self.root.configure(bg="#2c3e50")  # Fondo oscuro

        # Título principal
        title = tk.Label(root, text="Análisis Léxico y Expresiones Regulares", bg="#34495e", fg="white", font=("Arial", 18))
        title.pack(fill=tk.X)

        # Área de texto para cargar archivo
        self.text_area = tk.Text(root, wrap="word", height=10, bg="#ecf0f1", fg="black", font=("Arial", 12))
        self.text_area.pack(expand=1, fill="both", padx=10, pady=10)

        # Área para mostrar los resultados
        self.resultado = tk.Text(root, wrap="word", state="disabled", height=10, bg="#bdc3c7", fg="black", font=("Arial", 12))
        self.resultado.pack(expand=1, fill="both", padx=10, pady=10)

        # Menú superior
        self.menu = tk.Menu(root)
        root.config(menu=self.menu)

        file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Abrir", command=self.abrir_archivo)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=root.quit)

        # Botones para análisis léxico y expresiones regulares
        button_frame = tk.Frame(root, bg="#2c3e50")
        button_frame.pack(fill=tk.X)

        lex_btn = tk.Button(button_frame, text="Análisis Léxico", command=self.realizar_analisis_lexico, bg="#3498db", fg="white", font=("Arial", 12))
        lex_btn.pack(side="left", padx=10, pady=5)

        afd_btn = tk.Button(button_frame, text="Análisis Expresiones Regulares", command=self.realizar_analisis_afd, bg="#e74c3c", fg="white", font=("Arial", 12))
        afd_btn.pack(side="left", padx=10, pady=5)

        sem_btn = tk.Button(button_frame, text="Análisis Semántico", command=self.realizar_analisis_semantico, bg="#2ecc71", fg="white", font=("Arial", 12))
        sem_btn.pack(side="left", padx=10, pady=5)

    def abrir_archivo(self):
        archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
        if archivo:
            with open(archivo, "r") as file:
                contenido = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, contenido)

    def realizar_analisis_lexico(self):
        contenido = self.text_area.get(1.0, tk.END)
        resultado = analizar_archivo(contenido)
        self.mostrar_resultado_lexico(resultado)

    def realizar_analisis_afd(self):
        contenido = self.text_area.get(1.0, tk.END)
        afd = RegexToAFD(contenido.strip())  # Crear el autómata con la expresión regular ingresada
        cadena = tk.simpledialog.askstring("Entrada", "Ingrese la cadena a evaluar:")
        if afd.test_string(cadena):
            resultado = f"'{cadena}' es válida según la expresión '{contenido}'\n"
        else:
            resultado = f"'{cadena}' NO es válida según la expresión '{contenido}'\n"
        self.mostrar_resultado(resultado)

    def realizar_analisis_semantico(self):
        contenido = self.text_area.get(1.0, tk.END)
        resultado = analizar_semantica(contenido)
        self.mostrar_resultado(resultado)

    def mostrar_resultado_lexico(self, resultado):
        self.resultado.config(state="normal")
        self.resultado.delete(1.0, tk.END)
        for numero_linea, tokens in resultado:
            self.resultado.insert(tk.END, f"Línea {numero_linea}:\n")
            for token, tipo in tokens:
                self.resultado.insert(tk.END, f"  {token} -> {tipo}\n")
        self.resultado.config(state="disabled")

    def mostrar_resultado(self, resultado):
        self.resultado.config(state="normal")
        self.resultado.delete(1.0, tk.END)
        self.resultado.insert(tk.END, resultado)
        self.resultado.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = AnalizadorApp(root)
    root.mainloop()
