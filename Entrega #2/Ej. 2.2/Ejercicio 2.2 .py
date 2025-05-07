from enum import Enum

class TipoPlaneta(Enum):
    GASEOSO = "GASEOSO"
    TERRESTRE = "TERRESTRE"
    ENANO = "ENANO"

class Planeta():
    def __init__(self, nombre, cantidadSatelites, masa, volumen, diametro, distanciaSol, tipo, esObservable):
        self.nombre = nombre
        self.cantidadSatelites = cantidadSatelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distanciaSol = distanciaSol
        self.tipo = tipo
        self.esObservable = esObservable

    def imprimir(self):
        print(f"Nombre del planeta = {self.nombre}")
        print(f"Cantidad de satélites = {self.cantidadSatelites}")
        print(f"Masa del planeta = {self.masa}")
        print(f"Volumen del planeta = {self.volumen}")
        print(f"Diámetro del planeta = {self.diametro}")
        print(f"Distancia al sol = {self.distanciaSol}")
        print(f"Tipo de planeta = {self.tipo.value}")
        print(f"Es observable = {self.esObservable}")

    def calcularDensidad(self):
        return self.masa / self.volumen

    def esPlanetaExterior(self):
        limite = 149597870 * 3.4
        return self.distanciaSol > limite

if __name__ == "__main__":
    p1 = Planeta("Tierra", 1, 5.9736e24, 1.08321e12, 12742, 150000000, TipoPlaneta.TERRESTRE, True)
    p1.imprimir()
    print(f"Densidad del planeta = {p1.calcularDensidad()}")
    print(f"Es planeta exterior = {p1.esPlanetaExterior()}\n")

    p2 = Planeta("Júpiter", 79, 1.899e27, 1.4313e15, 139820, 750000000, TipoPlaneta.GASEOSO, True)
    p2.imprimir()
    print(f"Densidad del planeta = {p2.calcularDensidad()}")
    print(f"Es planeta exterior = {p2.esPlanetaExterior()}")