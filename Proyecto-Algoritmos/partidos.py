class partidos():

    def __init__(self, equipo_local, equipo_visitante, fecha_hora, estadio, id):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.fecha_hora = fecha_hora
        self.estadio = estadio
        self.id = id


    def mostrar(self):
        print(f"\n{self.equipo_local} contra {self.equipo_visitante} el {self.fecha_hora} en el estadio {self.estadio} id del partido {self.id}")

