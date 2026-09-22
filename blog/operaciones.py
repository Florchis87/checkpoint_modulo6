from blog.modelos import Autor, Post


def crear_post(blog):
    print("\n--- CREAR NUEVO POST ---")

    titulo = input("Título: ").strip()
    contenido = input("Contenido: ").strip()

    if not titulo or not contenido:
        print("El título y el contenido no pueden estar vacíos.")
        return

    nombre_autor = input("Nombre del autor: ").strip()
    bio_autor = input("Bio del autor: ").strip()
    especialidad = input("Especialidad del autor: ").strip()

    autor = Autor(
        nombre_autor,
        bio_autor,
        especialidad
    )

    tags_texto = input("Tags separados por coma: ")
    tags = [tag.strip() for tag in tags_texto.split(",") if tag.strip()]

    estado = input("Estado (borrador/publicado/archivado): ").strip().lower()

    nuevo_id = len(blog.posts) + 1

    nuevo_post = Post(
        nuevo_id,
        titulo,
        contenido,
        autor,
        tags,
        estado
    )

    blog.agregar_post(nuevo_post)

    print("¡Post creado correctamente!")