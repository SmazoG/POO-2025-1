from cilindro import *

class VentanaCilindro(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Cilindro")
        self.geometry("280x210")
        self.resizable(False, False)
        self.configurar_interfaz()
    
    def configurar_interfaz(self):
        # Etiquetas y campos
        tk.Label(self, text="Radio (cms):").place(x=20, y=20)
        self.campo_radio = tk.Entry(self)
        self.campo_radio.place(x=100, y=20, width=135)
        
        tk.Label(self, text="Altura (cms):").place(x=20, y=50)
        self.campo_altura = tk.Entry(self)
        self.campo_altura.place(x=100, y=50, width=135)
        
        # Botón de cálculo
        btn_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        btn_calcular.place(x=100, y=80, width=135)
        
        # Resultados
        self.volumen = tk.Label(self, text="Volumen (cm3):")
        self.volumen.place(x=20, y=110)
        
        self.superficie = tk.Label(self, text="Superficie (cm2):")
        self.superficie.place(x=20, y=140)
    
    def calcular(self):
        try:
            radio = float(self.campo_radio.get())
            altura = float(self.campo_altura.get())
            cilindro = Cilindro(radio, altura)
            
            self.volumen.config(text=f"Volumen (cm3): {cilindro.get_volumen():.2f}")
            self.superficie.config(text=f"Superficie (cm2): {cilindro.get_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")