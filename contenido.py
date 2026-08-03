class Contenido:
    def __init__(self, id, titulo, autor, anio, num_reproducciones):
        self.id = id 
        self.titulo = titulo 
        self.autor = autor
        self.anio = anio
        self.reproducciones = num_reproducciones

class Musica(Contenido):
    def __init__(self, id, autor, titulo, anio, num_reproducciones, duracion, genero):
        super().__init__(id, titulo, autor, anio, num_reproducciones)
        self.duracion = duracion 
        self.genero = genero

class Podcast(Contenido):
    def __init__(self, id, autor, titulo, anio, num_reproducciones, num_episodios, tematica):
        super().__init__(id, titulo, autor, anio, num_reproducciones)
        self.episodios = num_episodios
        self.tematica = tematica
    