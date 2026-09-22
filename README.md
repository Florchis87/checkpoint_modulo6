# Blog de Jane Austen

## Descripción

Este proyecto consiste en un blog desarrollado en Python sobre Jane Austen.

En esta versión se realizó una refactorización del proyecto anterior utilizando Programación Orientada a Objetos (POO) y persistencia de datos mediante archivos JSON.

El programa permite gestionar posts desde la consola, buscarlos, filtrarlos, validarlos, crear nuevos posts y guardar la información para que permanezca disponible al volver a ejecutar el programa.

## Tecnologías utilizadas

- Python
- Programación Orientada a Objetos (POO)
- JSON
- Visual Studio Code

## Estructura del proyecto

```text
BLOG_CONSOLA/
│
├── blog/
│   ├── __init__.py
│   ├── datos.py
│   ├── menu.py
│   ├── modelos.py
│   ├── operaciones.py
│   └── validaciones.py
│
├── main.py
├── posts.json
└── README.md

Clases principales
Autor

Representa al autor de los posts.

Sus principales atributos son:

nombre
bio
especialidad
redes_sociales

También permite convertir el objeto a diccionario y reconstruirlo desde un diccionario.

Post

Representa una publicación del blog.

Sus atributos son:

id
titulo
contenido
autor
tags
estado

El atributo autor utiliza un objeto de la clase Autor.

Blog

Es la clase principal encargada de gestionar los posts.

Permite:

listar posts
buscar posts por título
filtrar posts por tag
agregar nuevos posts
obtener los posts
validar los posts
Persistencia de datos

Los datos se almacenan en el archivo posts.json.

El archivo permite guardar la información de los posts para que no se pierda cuando se cierra el programa.

El proyecto utiliza métodos de conversión entre objetos y diccionarios para poder trabajar con JSON:

to_dict() convierte objetos en diccionarios.
from_dict() convierte diccionarios en objetos.
Funcionalidades

El programa cuenta con un menú de consola con las siguientes opciones:

Ver todos los posts
Buscar por título
Filtrar por tag
Crear nuevo post
Validar posts
Guardar posts en JSON
Salir
Manejo de errores

El programa contempla diferentes situaciones, como:

archivo JSON inexistente
archivo JSON vacío
JSON inválido
campos obligatorios vacíos
estado de post no válido
tipos de datos incorrectos
Cómo ejecutar el proyecto
Abrir la carpeta del proyecto en Visual Studio Code.
Abrir una terminal.
Ejecutar:
python main.py
Utilizar el menú de opciones para interactuar con el blog.
Autor

Proyecto realizado como parte de la cursada de Python.