from enum import Enum

class TipoCom(Enum):
    GASOLINA = "GASOLINA"
    BIOETANOL = "BIOETANOL"
    DIESEL = "DIESEL"
    BIODIESEL = "BIODIESEL"
    GAS_NATURAL = "GAS_NATURAL"

class TipoA(Enum):
    CIUDAD = "CIUDAD"
    SUBCOMPACTO = "SUBCOMPACTO"
    COMPACTO = "COMPACTO"
    FAMILIAR = "FAMILIAR"
    EJECUTIVO = "EJECUTIVO"
    SUV = "SUV"

class TipoColor(Enum):
    BLANCO = "BLANCO"
    NEGRO = "NEGRO"
    ROJO = "ROJO"
    NARANJA = "NARANJA"
    AMARILLO = "AMARILLO"
    VERDE = "VERDE"
    AZUL = "AZUL"
    VIOLETA = "VIOLETA"

class Automovil:
    def __init__(self, marca, modelo, motor, tipoCombustible, tipoAutomovil, 
                 numeroPuertas, cantidadAsientos, velocidadMaxima, color):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipoCombustible = tipoCombustible
        self.tipoAutomovil = tipoAutomovil
        self.numeroPuertas = numeroPuertas
        self.cantidadAsientos = cantidadAsientos
        self.velocidadMaxima = velocidadMaxima
        self.color = color
        self.velocidadActual = 0

    def getMarca(self): return self.marca
    def setMarca(self, marca): self.marca = marca
        
    def getModelo(self): return self.modelo
    def setModelo(self, modelo): self.modelo = modelo
        
    def getMotor(self): return self.motor
    def setMotor(self, motor): self.motor = motor
        
    def getTipoCombustible(self): return self.tipoCombustible
    def setTipoCombustible(self, tipoCombustible): self.tipoCombustible = tipoCombustible
        
    def getTipoAutomovil(self): return self.tipoAutomovil
    def setTipoAutomovil(self, tipoAutomovil): self.tipoAutomovil = tipoAutomovil
        
    def getNumeroPuertas(self): return self.numeroPuertas
    def setNumeroPuertas(self, numeroPuertas): self.numeroPuertas = numeroPuertas
        
    def getCantidadAsientos(self): return self.cantidadAsientos
    def setCantidadAsientos(self, cantidadAsientos): self.cantidadAsientos = cantidadAsientos
        
    def getVelocidadMaxima(self): return self.velocidadMaxima
    def setVelocidadMaxima(self, velocidadMaxima): self.velocidadMaxima = velocidadMaxima
        
    def getColor(self): return self.color
    def setColor(self, color): self.color = color
        
    def getVelocidadActual(self): return self.velocidadActual
    def setVelocidadActual(self, velocidadActual): self.velocidadActual = velocidadActual

    def acelerar(self, incrementoVelocidad):
        if self.velocidadActual + incrementoVelocidad < self.velocidadMaxima:
            self.velocidadActual += incrementoVelocidad
        else:
            print("No se puede incrementar a una velocidad superior a la maxima del automovil.")

    def desacelerar(self, decrementoVelocidad):
        if (self.velocidadActual - decrementoVelocidad) > 0:
            self.velocidadActual -= decrementoVelocidad
        else:
            print("No se puede decrementar a una velocidad negativa.")

    def frenar(self): self.velocidadActual = 0

    def calcularTiempoLlegada(self, distancia):
        return distancia / self.velocidadActual if self.velocidadActual != 0 else 0

    def imprimir(self):
        print(f"Marca = {self.marca}")
        print(f"Modelo = {self.modelo}")
        print(f"Motor = {self.motor}")
        print(f"Tipo de combustible = {self.tipoCombustible.value}")
        print(f"Tipo de automovil = {self.tipoAutomovil.value}")
        print(f"Numero de puertas = {self.numeroPuertas}")
        print(f"Cantidad de asientos = {self.cantidadAsientos}")
        print(f"Velocidad maxima = {self.velocidadMaxima}")
        print(f"Color = {self.color.value}")

if __name__ == "__main__":
    auto1 = Automovil("Ford", 2018, 3, TipoCom.DIESEL, TipoA.EJECUTIVO, 
                      5, 6, 250, TipoColor.NEGRO)
    auto1.imprimir()
    auto1.setVelocidadActual(100)
    print(f"Velocidad actual = {auto1.velocidadActual}")
    auto1.acelerar(20)
    print(f"Velocidad actual = {auto1.velocidadActual}")
    auto1.desacelerar(50)
    print(f"Velocidad actual = {auto1.velocidadActual}")
    auto1.frenar()
    print(f"Velocidad actual = {auto1.velocidadActual}")
    auto1.desacelerar(20)