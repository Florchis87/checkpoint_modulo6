Blog de Jane Austen

## Descripción

Este proyecto es un sistema de blog por consola desarrollado en Python.

El programa permite listar posts, buscar posts por título, filtrar posts por tag y validar la información de los posts.

El proyecto está organizado mediante módulos y paquetes para separar las responsabilidades y facilitar su lectura y mantenimiento.

## Cómo ejecutar el programa

Para ejecutar el sistema, abrir la terminal desde la carpeta raíz del proyecto y escribir:

```bash
```
python main.py

## Estructura del proyecto

blog_consola/
│
├── main.py
├── README.md
│
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── operaciones.py
    └── validaciones.py

## Responsabilidad de cada archivo

main.py
Es el archivo principal del programa. Coordina el funcionamiento del sistema, muestra el menú y llama a las funciones correspondientes.

blog/datos.py
Contiene las estructuras de datos del blog, incluyendo la información de la autora, los estados, las etiquetas y los posts.

blog/menu.py
Contiene la función encargada de mostrar el menú y recibir la opción elegida por el usuario.

blog/operaciones.py
Contiene las funciones para listar posts, buscar por título y filtrar por tag.

blog/validaciones.py
Contiene las reglas utilizadas para comprobar que los posts tengan una estructura válida.

blog/init.py
Permite organizar la carpeta blog como un paquete de Python.

## Funcionalidades
El sistema cuenta con las siguientes opciones:

Ver todos los posts.
Buscar por título.
Filtrar por tag.
Validar posts.
Salir del programa.
Autora

Los posts utilizados en este proyecto están relacionados con la escritora Jane Austen.

