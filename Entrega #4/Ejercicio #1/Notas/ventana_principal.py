import tkinter as tk
from notas import *
class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Notas")
        self.geometry("280x380")
        self.resizable(False, False)
        self.configurar_interfaz()
        
    def configurar_interfaz(self):
        # Crear campos de texto para notas
        self.campos_notas = []
        for i in range(5):
            etiqueta = tk.Label(self, text=f"Nota {i+1}:")
            etiqueta.place(x=20, y=20 + i*30)
            
            campo = tk.Entry(self, width=10)
            campo.place(x=105, y=20 + i*30)
            self.campos_notas.append(campo)
        
        # Botones
        self.btn_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        self.btn_calcular.place(x=20, y=170, width=100)
        
        self.btn_limpiar = tk.Button(self, text="Limpiar", command=self.limpiar)
        self.btn_limpiar.place(x=125, y=170, width=80)
        
        # Etiquetas de resultados
        self.resultados = {
            'promedio': tk.Label(self, text="Promedio = "),
            'desviacion': tk.Label(self, text="Desviación estándar = "),
            'mayor': tk.Label(self, text="Nota mayor = "),
            'menor': tk.Label(self, text="Nota menor = ")
        }
        
        # Posicionar resultados
        for i, key in enumerate(self.resultados.keys()):
            self.resultados[key].place(x=20, y=210 + i*30)

    def calcular(self):
        notas = Notas()
        
        try:
            for i in range(5):
                valor = float(self.campos_notas[i].get())
                notas.lista_notas[i] = valor
        except ValueError:
            tk.messagebox.showerror("Error", "Ingrese valores numéricos válidos")
            return

        # Actualizar resultados
        self.resultados['promedio'].config(
            text=f"Promedio = {notas.calcular_promedio():.2f}"
        )
        self.resultados['desviacion'].config(
            text=f"Desviación estándar = {notas.calcular_desviacion():.2f}"
        )
        self.resultados['mayor'].config(
            text=f"Nota mayor = {notas.calcular_mayor():.2f}"
        )
        self.resultados['menor'].config(
            text=f"Nota menor = {notas.calcular_menor():.2f}"
        )

    def limpiar(self):
        for campo in self.campos_notas:
            campo.delete(0, tk.END)
        for resultado in self.resultados.values():
            resultado.config(text=resultado.cget('text').split('=')[0] + '= ')
