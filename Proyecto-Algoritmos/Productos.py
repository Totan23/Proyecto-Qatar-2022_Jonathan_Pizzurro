class productos():
    def __init__(self, nombre, cantidad, precio, tipo, adicional):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio + (precio * 0.16)
        self.tipo = tipo
        self.adicional = adicional



    def mostrar(self):
        print(f"nombre: {self.nombre}\n precio: {self.precio}\n tipo: {self.tipo}")

