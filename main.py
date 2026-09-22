from blog.datos import cargar_posts, guardar_posts
from blog.menu import mostrar_menu
from blog.operaciones import crear_post
from blog.modelos import Blog


RUTA_JSON = "posts.json"
ESTADOS_VALIDOS = ("borrador", "publicado", "archivado")


def ejecutar_blog():
    posts = cargar_posts(RUTA_JSON)
    blog = Blog(posts)

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            blog.listar_posts()

        elif opcion == "2":
            termino = input("Ingresá el título que querés buscar: ")
            resultados = blog.buscar_por_titulo(termino)

            if resultados:
                blog_resultados = Blog(resultados)
                blog_resultados.listar_posts()
            else:
                print("No se encontraron posts.")

        elif opcion == "3":
            tag = input("Ingresá el tag que querés buscar: ")
            resultados = blog.filtrar_por_tag(tag)

            if resultados:
                blog_resultados = Blog(resultados)
                blog_resultados.listar_posts()
            else:
                print("No se encontraron posts con ese tag.")

        elif opcion == "4":
            crear_post(blog)

        elif opcion == "5":
            resultados = blog.validar_posts(ESTADOS_VALIDOS)

            for post, errores in resultados:
                print(f"\nPost: {post.titulo}")

                if errores:
                    print("El post tiene errores:")
                    for error in errores:
                        print("-", error)
                else:
                    print("El post es válido.")

        elif opcion == "6":
            guardar_posts(RUTA_JSON, blog.obtener_posts())
            print("Posts guardados correctamente.")

        elif opcion == "7":
            print("¡Gracias por usar el blog!")
            break

        else:
            print("Opción inválida. Elegí una opción del 1 al 7.")


if __name__ == "__main__":
    ejecutar_blog()