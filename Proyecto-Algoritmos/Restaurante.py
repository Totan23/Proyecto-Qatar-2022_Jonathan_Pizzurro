class restaurante():
    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos


    def mostrar(self):
        print(f"nombre: {self.nombre}\n productos: {self.productos} ")

