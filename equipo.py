class Equipo:
    def __init__(self):
        self.empleados = []

    def agregar_individualmente(self, empleado):
        bandera = False
        for i in self.empleados:
            if empleado.id == i.id:
                print("Este id ya se encuentra registrado en el Equipo, inténtelo con otro")
                bandera = True
                break
        if not(bandera):
            self.empleados.append(empleado)
            print("Inserción exitosa")

    def mostrar_equipo(self):
        self.empleados.sort(key=lambda X: X.nombre)
        print("LISTA DE EMPLEADOS")
        for empleado in self.empleados:
            print(f"{empleado.id}: Se llama {empleado.nombre} y tiene el cargo de {empleado.cargo} en el departamento de {empleado.departamento}")
