import ply.yacc as yacc
from lexer import tokens


# Reglas de gramática
def p_statement_expr(p):
    "statement : expression SEMICOLON"
    print("Expresión válida:", p[1])


def p_expression_binop(p):
    """expression : expression PLUS expression
    | expression MINUS expression
    | expression MULTIPLY expression
    | expression DIVIDE expression"""
    p[0] = f"({p[1]} {p[2]} {p[3]})"


def p_expression_group(p):
    "expression : LPAREN expression RPAREN"
    p[0] = p[2]


def p_expression_number(p):
    "expression : NUMBER"
    p[0] = p[1]


def p_expression_variable(p):
    "expression : VARIABLE"
    p[0] = p[1]


def p_error(p):
    print("Error de parsing:", p)


# Construir el parser
parser = yacc.yacc()
