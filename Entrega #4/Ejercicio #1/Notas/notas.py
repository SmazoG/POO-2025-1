import math

class Notas:
    def __init__(self):
        self.lista_notas = [0.0] * 5  # Inicializa con 5 ceros

    def calcular_promedio(self):
        suma = sum(self.lista_notas)
        return suma / len(self.lista_notas)

    def calcular_desviacion(self):
        promedio = self.calcular_promedio()
        suma = 0.0
        for nota in self.lista_notas:
            suma += math.pow(nota - promedio, 2)
        return math.sqrt(suma / len(self.lista_notas))

    def calcular_menor(self):
        return min(self.lista_notas)

    def calcular_mayor(self):
        return max(self.lista_notas)