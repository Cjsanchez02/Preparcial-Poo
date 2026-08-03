class Catalogo:
    def __init__(self):
        self.contenido = []

    def agregar_individualmente(self, multimedia):
        bandera = True 
        for i in self.contenido:
            if i.id == multimedia.id:
                print("Este ID ya se encuentra registrado en el catalogo")
                bandera = False
                break
        if bandera:
            self.contenido.append(multimedia)
            print("Operacion exitosa")

    def mostrar_contenido(self):
        self.contenido.sort(key=lambda X: X.id)
        print("LISTA DE CONTENIDOS")
        for i in self.contenido:
            print(f"{i.id}: {i.titulo} fue hecha por {i.autor} en el año {i.anio} y tiene {i.reproducciones} reproducciones")

    def simular_reproduccion(self, id):
        bandera = True
        for i in self.contenido:
            if i.id == id:
                i.reproducciones += 1
                print("Operacion exitosa")
                bandera = False
                break
        if bandera == True:
            print("No se encontró el ID del contenido a reproducir, vuelvalo a intentar.")