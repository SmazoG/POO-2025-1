from ventana_cilindro import *
from ventana_esfera import *
from ventana_piramide import *



class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras Geométricas")
        self.geometry("350x160")
        self.resizable(False, False)
        self.configurar_interfaz()
    
    def configurar_interfaz(self):
        # Botones para figuras
        btn_cilindro = tk.Button(self, text="Cilindro", command=self.abrir_cilindro)
        btn_cilindro.place(x=20, y=50, width=80, height=30)
        
        btn_esfera = tk.Button(self, text="Esfera", command=self.abrir_esfera)
        btn_esfera.place(x=125, y=50, width=80, height=30)
        
        btn_piramide = tk.Button(self, text="Pirámide", command=self.abrir_piramide)
        btn_piramide.place(x=230, y=50, width=80, height=30)
    
    def abrir_cilindro(self):
        VentanaCilindro()
    
    def abrir_esfera(self):
        VentanaEsfera()
    
    def abrir_piramide(self):
        VentanaPiramide()