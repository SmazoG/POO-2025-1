import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcularArea(self):
        return math.pi * (self.radio ** 2)

    def calcularPerimetro(self):
        return 2 * math.pi * self.radio


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

    def calcularPerimetro(self):
        return 2 * self.base + 2 * self.altura
        
        
class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcularArea(self):
        return self.lado ** 2

    def calcularPerimetro(self):
        return 4 * self.lado
        

class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura / 2

    def calcularPerimetro(self):
        return self.base + self.altura + self.calcularHipotenusa()

    def calcularHipotenusa(self):
        return math.sqrt(self.base**2 + self.altura**2)

    def determinarTipoTriangulo(self):
        hipotenusa = self.calcularHipotenusa()
        if self.base == self.altura == hipotenusa:
            print("Es un triangulo equilatero")
        elif self.base != self.altura and self.base != hipotenusa and self.altura != hipotenusa:
            print("Es un triangulo escaleno")
        else:
            print("Es un triangulo isosceles")

class PruebaFiguras:
    def main(self):
        figura1 = Circulo(2)
        figura2 = Rectangulo(1, 2)
        figura3 = Cuadrado(3)
        figura4 = TrianguloRectangulo(3, 5)
    
        print(f"El área del círculo es = {figura1.calcularArea():.2f}")
        print(f"El perímetro del círculo es = {figura1.calcularPerimetro():.2f}\n")
    
        print(f"El área del rectángulo es = {figura2.calcularArea():.2f}")
        print(f"El perímetro del rectángulo es = {figura2.calcularPerimetro():.2f}\n")
    
        print(f"El área del cuadrado es = {figura3.calcularArea():.2f}")
        print(f"El perímetro del cuadrado es = {figura3.calcularPerimetro():.2f}\n")
    
        print(f"El área del triángulo es = {figura4.calcularArea():.2f}")
        print(f"El perímetro del triángulo es = {figura4.calcularPerimetro():.2f}")
        figura4.determinarTipoTriangulo()
        
        
if __name__ == "__main__":
  pruebafiguras = PruebaFiguras()
  pruebafiguras.main()
