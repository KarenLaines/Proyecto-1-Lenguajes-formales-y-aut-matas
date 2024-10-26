import re
from tkinter import messagebox

# Clase para manejar la conversión de expresiones regulares a AFD
class RegexToAFD:
    def __init__(self, regex):
        self.regex = regex
        try:
            self.pattern = re.compile(self.regex)  # Intentar compilar la expresión regular
        except re.error:
            messagebox.showerror("Error", "Expresión regular no válida.")
            self.pattern = None

    def test_string(self, string):
        if self.pattern:
            # Este método prueba si la cadena cumple con la expresión regular
            return bool(self.pattern.fullmatch(string))
        return False
