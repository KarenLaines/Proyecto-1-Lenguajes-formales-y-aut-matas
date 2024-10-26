import ply.lex as lex

# Lista de tokens
tokens = [
    "VARIABLE",
    "NUMBER",
    "PLUS",
    "MINUS",
    "MULTIPLY",
    "DIVIDE",
    "LPAREN",
    "RPAREN",
    "ASSIGN",
    "SEMICOLON",
    "IF",
    "ELSE",
    "WHILE",
    "FUNC",
    "COMMA",
]

# Reglas de expresión regular para tokens
t_PLUS = r"\+"
t_MINUS = r"-"
t_MULTIPLY = r"\*"
t_DIVIDE = r"/"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_ASSIGN = r"="
t_SEMICOLON = r";"
t_COMMA = r","

# Palabras clave
reserved = {
    "if": "IF",
    "else": "ELSE",
    "while": "WHILE",
    "func": "FUNC",
}


# Reglas para tokens
def t_VARIABLE(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"
    t.type = reserved.get(t.value, "VARIABLE")  # Verifica si es una palabra clave
    return t


def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t


# Ignorar espacios y tabulaciones
t_ignore = " \t"


# Manejo de errores
def t_error(t):
    print(f"Error de lexing: {t.value[0]}")
    t.lexer.skip(1)


# Construir el lexer
lexer = lex.lex()
