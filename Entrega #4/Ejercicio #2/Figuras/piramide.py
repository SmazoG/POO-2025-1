from figura_geometrica import *
import tkinter as tk

class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())
    
    def calcular_volumen(self):
        return (self.base ** 2 * self.altura) / 3.0
    
    def calcular_superficie(self):
        area_base = self.base ** 2
        area_lateral = 4 * (self.base * self.apotema) / 2  # 4 caras triangulares
        return area_base + area_lateral