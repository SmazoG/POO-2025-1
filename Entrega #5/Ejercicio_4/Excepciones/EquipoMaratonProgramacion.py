class EquipoMaratonProgramacion:
    def __init__(self, nombre_equipo, universidad, lenguaje_programacion):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje_programacion = lenguaje_programacion
        self.tamaño_equipo = 0
        self.programadores = [None, None, None]  # Array para 3 programadores
    
    def esta_lleno(self):
        return self.tamaño_equipo == len(self.programadores)
    
    def añadir_programador(self, programador):
        if self.esta_lleno():
            raise Exception("El equipo está completo. No se pudo agregar programador.")
        
        self.programadores[self.tamaño_equipo] = programador
        self.tamaño_equipo += 1
    
    def listar_programadores(self):
        return [str(p) for p in self.programadores if p is not None]
    
    @staticmethod
    def validar_campo(campo):
        if any(char.isdigit() for char in campo):
            raise Exception("El nombre no puede tener dígitos.")
        
        if len(campo) > 20:
            raise Exception("La longitud no debe ser superior a 20 caracteres.")

