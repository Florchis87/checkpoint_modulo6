def listar_posts(lista):
    for post in lista:
        print("Título:", post["titulo"])
        print("Autor:", post["autor"]["nombre"])
        print("Estado:", post["estado"])
        print("--------------------")


def buscar_por_titulo(lista, termino):
    resultados = []

    for post in lista:
        if termino.lower() in post["titulo"].lower():
            resultados.append(post)

    return resultados


def filtrar_por_tag(lista, tag):
    resultados = []

    for post in lista:
        for etiqueta in post["tags"]:
            if etiqueta.lower() == tag.lower():
                resultados.append(post)
                break

    return resultados