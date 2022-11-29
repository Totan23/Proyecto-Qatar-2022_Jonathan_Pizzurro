class estadios():

    def __init__(self, id, nombre, capacidad, ubicacion, restaurantes):
        self.id = id
        self.nombre = nombre
        self.capacidad = capacidad
        self.ubicacion = ubicacion
        self.restaurantes = restaurantes



    def mostrar(self):
        print(f"id: {self.id} nombre: {self.nombre} capacidad: {self.capacidad} ubicacion: {self.ubicacion}")

