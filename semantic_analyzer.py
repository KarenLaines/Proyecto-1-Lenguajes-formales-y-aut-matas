def analizar_semantica(contenido):
    lineas = contenido.split("\n")
    resultado = []
    variables_declaradas = set()
    palabras_clave = {
        "entero",
        "decimal",
        "booleano",
        "cadena",
        "si",
        "sino",
        "mientras",
        "hacer",
        "verdadero",
        "falso",
    }

    for numero_linea, linea in enumerate(lineas, start=1):
        tokens = linea.split()

        # Regla: Verificar declaración de variables
        if (
            "entero" in tokens
            or "decimal" in tokens
            or "booleano" in tokens
            or "cadena" in tokens
        ):
            # Suponemos que la variable está después del tipo
            indice = (
                tokens.index("entero")
                if "entero" in tokens
                else (
                    tokens.index("decimal")
                    if "decimal" in tokens
                    else (
                        tokens.index("booleano")
                        if "booleano" in tokens
                        else tokens.index("cadena")
                    )
                )
            )
            if indice + 1 < len(tokens):
                variables_declaradas.add(tokens[indice + 1])

        # Regla: Verificar uso de variables
        for token in tokens:
            if (
                token not in variables_declaradas
                and token not in palabras_clave
                and token.isidentifier()
            ):
                resultado.append(
                    f"Error semántico en línea {numero_linea}: La variable '{token}' no está declarada."
                )
                break
        else:
            resultado.append(f"Línea {numero_linea} está correcta.")

    return "\n".join(resultado)
