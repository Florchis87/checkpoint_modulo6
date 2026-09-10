def validar_post(post, estados_validos):
    errores = []

    if not isinstance(post, dict):
        errores.append("El post no es un diccionario.")
        return errores

    if "titulo" not in post:
        errores.append("Falta el título.")
    elif post["titulo"].strip() == "":
        errores.append("El título está vacío.")

    if "contenido" not in post:
        errores.append("Falta el contenido.")
    elif post["contenido"].strip() == "":
        errores.append("El contenido está vacío.")

    if "autor" not in post:
        errores.append("Falta el autor.")
    elif not isinstance(post["autor"], dict):
        errores.append("El autor no es un diccionario.")
    elif "nombre" not in post["autor"]:
        errores.append("El autor no tiene nombre.")

    if "tags" not in post:
        errores.append("Faltan los tags.")
    elif not isinstance(post["tags"], list):
        errores.append("Los tags no están guardados como lista.")

    if "estado" not in post:
        errores.append("Falta el estado.")
    elif post["estado"] not in estados_validos:
        errores.append("El estado no es válido.")

    return errores