from figura_geometrica import *
import tkinter as tk

class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())
    
    def calcular_volumen(self):
        return math.pi * self.altura * (self.radio ** 2)
    
    def calcular_superficie(self):
        area_lateral = 2 * math.pi * self.radio * self.altura
        area_base = 2 * math.pi * (self.radio ** 2)
        return area_lateral + area_base