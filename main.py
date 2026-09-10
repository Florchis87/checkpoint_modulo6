from blog.datos import posts, estados_post
from blog.menu import mostrar_menu
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_post


def ejecutar_blog():
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            listar_posts(posts)

        elif opcion == "2":
            termino = input("Ingresá el título que querés buscar: ")
            resultados = buscar_por_titulo(posts, termino)

            if resultados:
                listar_posts(resultados)
            else:
                print("No se encontraron posts.")

        elif opcion == "3":
            tag = input("Ingresá el tag que querés buscar: ")
            resultados = filtrar_por_tag(posts, tag)

            if resultados:
                listar_posts(resultados)
            else:
                print("No se encontraron posts con ese tag.")

        elif opcion == "4":
            for post in posts:
                errores = validar_post(post, estados_post)

                if errores:
                    print(f"\nPost: {post.get('titulo', 'Sin título')}")
                    print("El post tiene errores:")
                    for error in errores:
                        print("-", error)
                else:
                    print(f"\nPost: {post['titulo']}")
                    print("El post es válido.")

        elif opcion == "5":
            print("¡Gracias por usar el blog!")
            break

        else:
            print("Opción inválida. Elegí una opción del 1 al 5.")


if __name__ == "__main__":
    ejecutar_blog()