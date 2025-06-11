from esfera import *

class VentanaEsfera(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Esfera")
        self.geometry("280x200")
        self.resizable(False, False)
        self.configurar_interfaz()
    
    def configurar_interfaz(self):
        # Etiquetas y campos
        tk.Label(self, text="Radio (cms):").place(x=20, y=20)
        self.campo_radio = tk.Entry(self)
        self.campo_radio.place(x=100, y=20, width=135)
        
        # Botón de cálculo
        btn_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        btn_calcular.place(x=100, y=50, width=135)
        
        # Resultados
        self.volumen = tk.Label(self, text="Volumen (cm3):")
        self.volumen.place(x=20, y=90)
        
        self.superficie = tk.Label(self, text="Superficie (cm2):")
        self.superficie.place(x=20, y=120)
    
    def calcular(self):
        try:
            radio = float(self.campo_radio.get())
            esfera = Esfera(radio)
            
            self.volumen.config(text=f"Volumen (cm3): {esfera.get_volumen():.2f}")
            self.superficie.config(text=f"Superficie (cm2): {esfera.get_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")