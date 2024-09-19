import re

# Definición de tokens
TOKENS = {
    'PALABRA_RESERVADA': r'\b(entero|decimal|booleano|cadena|si|sino|mientras|hacer|verdadero|falso)\b',
    'OPERADOR': r'[\+\-\*/%=\(\){}]',
    'NUMERO': r'\b\d+\b',
    'IDENTIFICADOR': r'\b[a-zA-Z_]\w*\b',
    'SIGNO': r'[“”;]'
}

def analizar_linea(linea):
    tokens_encontrados = []
    for tipo, patron in TOKENS.items():
        for match in re.finditer(patron, linea):
            tokens_encontrados.append((match.group(), tipo))
    return tokens_encontrados

def analizar_archivo(contenido):
    lineas = contenido.split('\n')
    resultado = []
    for numero_linea, linea in enumerate(lineas, start=1):
        tokens = analizar_linea(linea)
        if tokens:
            resultado.append((numero_linea, tokens))
    return resultado
