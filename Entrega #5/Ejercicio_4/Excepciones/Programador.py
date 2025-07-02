class Programador:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"