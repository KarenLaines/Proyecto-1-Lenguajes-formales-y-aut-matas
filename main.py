import tkinter as tk
from tkinter import scrolledtext
from lexer import lexer  # Importar el lexer
from parser import parser  # Importar el parser


class CompilerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Compilador Simple")

        self.text_area = scrolledtext.ScrolledText(
            root, wrap=tk.WORD, width=50, height=20
        )
        self.text_area.pack(padx=10, pady=10)

        self.run_button = tk.Button(root, text="Ejecutar", command=self.run_code)
        self.run_button.pack(pady=5)

    def run_code(self):
        code = self.text_area.get("1.0", tk.END)
        lexer.input(code)
        for token in lexer:
            print(token)
        print("\nResultado del análisis sintáctico:")
        parser.parse(code)


# MAIN
if __name__ == "__main__":
    root = tk.Tk()
    app = CompilerApp(root)
    root.mainloop()
