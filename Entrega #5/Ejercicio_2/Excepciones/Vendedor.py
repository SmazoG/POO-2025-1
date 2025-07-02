class Vendedor:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = 0  # Valor inicial
    
    def imprimir(self):
        return (f"Nombre del vendedor = {self.nombre}\n"
                f"Apellidos del vendedor = {self.apellidos}\n"
                f"Edad del vendedor = {self.edad}")
    
    def verificar_edad(self, edad):
        # Lista para recolectar todos los errores
        errores = []
        
        # Validación 1: Edad fuera de rango
        if edad < 0 or edad > 120:
            errores.append("La edad no puede ser negativa ni mayor a 120.")
        
        # Validación 2: Menor de edad
        if edad < 18:
            errores.append("El vendedor debe ser mayor de 18 años.")
        
        # Si hay errores, lanzar excepción con todos los mensajes
        if errores:
            raise ValueError("\n".join(errores))
        
        self.edad = edad

