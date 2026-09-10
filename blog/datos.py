perfil_autor = {
    "nombre": "Jane Austen",
    "bio": "(1775_1817) fue una destacada novelista británica de la época "
    "georgiana, célebre por su ironía, su agudo ingenio y su minucioso análisis "
    "social de la aristocracia rural terrateniente",
    "especialidad": "Novelas románticas",
    "redes_sociales": ["@janeausten", "linkedin.com/in/janeausten"]
}
estados_post = ("borrador", "publicado", "archivado")
etiquetas_blog = {
    "Romance",
    "Sociedad",
    "Familia",
    "Matrimonio",
    "Amor",
    "Amistad",
    "Comedia",
    "Gótico",
    "Misterio",
    "Inglaterra",
}
posts = [
    {
        "id": 1,
        "titulo": "Orgullo y prejuicio",
        "autor": perfil_autor,
        "contenido": "Una historia sobre el amor, el matrimonio y las diferencias sociales.",
        "tags": ["Romance", "Sociedad", "Matrimonio", "Inglaterra"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Sentido y sensibilidad",
        "autor": perfil_autor,
        "contenido": "Una historia sobre dos hermanas que enfrentan el amor, las emociones y los cambios familiares.",
        "tags": ["Romance", "Familia", "Emociones", "Sociedad"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "Emma",
        "autor": perfil_autor,
        "contenido": "Una historia sobre amistad, amor y las situaciones creadas por las decisiones de Emma.",
        "tags": ["Romance", "Comedia", "Amistad", "Sociedad"],
        "estado": "archivado"
    }
]
