class Autor:
    def __init__(self, nombre, bio, especialidad="", redes_sociales=None):
        self.nombre = nombre
        self.bio = bio
        self.especialidad = especialidad
        self.redes_sociales = redes_sociales if redes_sociales is not None else []

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "bio": self.bio,
            "especialidad": self.especialidad,
            "redes_sociales": self.redes_sociales
        }

    @classmethod
    def from_dict(cls, datos):
        return cls(
            datos["nombre"],
            datos["bio"],
            datos.get("especialidad", ""),
            datos.get("redes_sociales", [])
        )

class Post:
    def __init__(self, id, titulo, contenido, autor, tags, estado):
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.tags = tags
        self.estado = estado

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.to_dict(),
            "tags": self.tags,
            "estado": self.estado
        }

    @classmethod
    def from_dict(cls, datos):
        autor = Autor.from_dict(datos["autor"])

        return cls(
            datos["id"],
            datos["titulo"],
            datos["contenido"],
            autor,
            datos["tags"],
            datos["estado"]
        )    

class Blog:
    def __init__(self, posts=None):
        self.posts = posts if posts is not None else []

    def listar_posts(self):
        for post in self.posts:
            print("Título:", post.titulo)
            print("Autor:", post.autor.nombre)
            print("Estado:", post.estado)
            print("--------------------")

    def buscar_por_titulo(self, termino):
        resultados = []

        for post in self.posts:
            if termino.lower() in post.titulo.lower():
                resultados.append(post)

        return resultados

    def filtrar_por_tag(self, tag):
        resultados = []

        for post in self.posts:
            for etiqueta in post.tags:
                if etiqueta.lower() == tag.lower():
                    resultados.append(post)
                    break

        return resultados

    def agregar_post(self, post):
        self.posts.append(post)

    def obtener_posts(self):
        return self.posts

    def validar_posts(self, estados_validos):
        resultados = []

        for post in self.posts:
            errores = []

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

            resultados.append((post, errores))

        return resultados

                