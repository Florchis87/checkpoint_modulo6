from blog.modelos import Autor, Post


def validar_post(post, estados_validos):
    errores = []

    if not isinstance(post, Post):
        errores.append("El post no es un objeto Post.")
        return errores

    if not post.titulo.strip():
        errores.append("El título está vacío.")

    if not post.contenido.strip():
        errores.append("El contenido está vacío.")

    if not isinstance(post.autor, Autor):
        errores.append("El autor no es un objeto Autor.")

    if not isinstance(post.tags, list):
        errores.append("Los tags no están guardados como lista.")

    if post.estado not in estados_validos:
        errores.append("El estado no es válido.")

    return errores