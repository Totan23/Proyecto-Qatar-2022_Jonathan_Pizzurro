class cliente():

    def __init__(self,nombre, edad, cedula, entradas):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula
        self.entradas = entradas
        
class entradas():

    def __init__(self, tipo, cantidad, id_partido, asiento):
        self.tipo = tipo
        self.cantidad = cantidad
        self.id_partido = id_partido
        self.asiento = asiento
        self.codigo = f"{self.id_partido}-{self.asiento}"