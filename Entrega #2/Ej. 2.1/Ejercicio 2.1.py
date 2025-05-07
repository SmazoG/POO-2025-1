class Persona():
  
  def __init__(self, nombre, apellido, documento_identidad, anio_nacimiento):
    self.nombre = nombre
    self.apellido = apellido
    self.documento_identidad = documento_identidad
    self.anio_nacimiento = anio_nacimiento
    
  def imprimir(self):
    print(f"Nombre = {self.nombre}\nApellido = {self.apellido}\nDocumento de Identidad = {self.documento_identidad}\nAño de nacimiento = {self.anio_nacimiento}\n")
  
if __name__ == "__main__":
  p1 = Persona("Pedro","Pérez","1053121010",1998)
  p2 = Persona("Luis","León","1053223344",2001)
  p1.imprimir()
  p2.imprimir()