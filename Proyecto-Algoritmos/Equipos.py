class equipos():

    def __init__(self, nombre, cod_FIFA, grupo, id):
        self.nombre = nombre
        self.cod_FIFA = cod_FIFA
        self.grupo = grupo
        self.id = id


    def mostrar(self):
        print(f"nombre del equipo: {self.nombre}\n codigo FIFA: {self.cod_FIFA}\n grupo: {self.grupo}\n id: {self.id}")

