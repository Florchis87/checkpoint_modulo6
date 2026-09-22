import json
import os

from blog.modelos import Autor, Post

def cargar_posts(ruta):
    if not os.path.exists(ruta):
        return []

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        if not datos:
            return []

        return [Post.from_dict(post) for post in datos]

    except (json.JSONDecodeError, KeyError, TypeError):
        return []

def guardar_posts(ruta, posts):
    datos = [post.to_dict() for post in posts]

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)    

        