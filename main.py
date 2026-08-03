from equipo import *
from contenido import *
from catalogo import *
from persona import *


def main():
    print("Bienvenido a nuestra aplicacion, y cuenta con las siguientes opciones")
    equipo = Equipo()
    catalogo = Catalogo()
    while True:
        opcion = int(input("1. Mostrar Contenido\n2. Mostrar Equipo.\n3. Agregar Empleado.\n4. Agregar Contenido.\n5. Simular Reproduccion\n6. Mostrar TOP 3.\n7. Eliminar contenido.\n8. Salir de la aplicacion: "))
        if opcion == 1:
            catalogo.mostrar_contenido()
        elif opcion == 2:
            equipo.mostrar_equipo()
        elif opcion == 3:
            nombre = input("Introduzca el nombre: ")
            id = input("Introduzca el id: ")
            cargo = input("Introduzca el cargo: ")
            departamento = input("Introduzca el departamento: ")
            equipo.agregar_individualmente(Persona(id, nombre, cargo, departamento))
        elif opcion == 4:
            titulo = input("Introduzca el tilulo: ")
            id = input("Introduzca el id: ")
            autor = input("Introduzca el autor: ")
            anio = input("Introduzca el año: ")
            reproducciones = input("Introduzca el numero de reproducciones: ")
            tipo = input("Introduzca el tipo de contenido").lower()
            if tipo == "musica":
                duracion = input("Introduzca la duracion de la cancion: ")
                genero = input("Introduzva el genero")
                catalogo.agregar_individualmente(Musica(id, titulo, autor, int(anio), int(reproducciones), int(duracion), genero))
            elif tipo == "podcast":
                episodios = int(input("Introdizca el numero de episodios"))
                tematica = input("Introduzca la tematica")
                catalogo.agregar_individualmente(Podcast(id, titulo, autor, anio, reproducciones, episodios, tematica))   
        elif opcion == 5:
            id = input("Introduzca el ID del contenido a reproducir")
        elif opcion == 6:
            pass
        elif opcion == 7:
            pass
        elif opcion == 8:
            print("Gracias por usar nuestra aplicacion")
            break

main()