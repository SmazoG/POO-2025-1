import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import math

class CalculosNumericosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculos Numéricos")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding=15)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        titulo = ttk.Label(main_frame, text="Cálculos Numéricos", 
                          font=("Arial", 14, "bold"))
        titulo.pack(pady=10)
        
        # Entrada de datos
        entrada_frame = ttk.LabelFrame(main_frame, text="Ingrese un valor numérico", padding=10)
        entrada_frame.pack(fill=tk.X, pady=10)
        
        # Campo de entrada
        self.entry_valor = ttk.Entry(entrada_frame)
        self.entry_valor.pack(fill=tk.X, padx=5, pady=5)
        
        # Botones de cálculo
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=10, fill=tk.X)
        
        btn_log = ttk.Button(btn_frame, text="Calcular Logaritmo", 
                            command=self.calcular_logaritmo)
        btn_log.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        btn_raiz = ttk.Button(btn_frame, text="Calcular Raíz Cuadrada", 
                             command=self.calcular_raiz)
        btn_raiz.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        # Botones adicionales (limpieza)
        btn_frame2 = ttk.Frame(main_frame)
        btn_frame2.pack(pady=5, fill=tk.X)
        
        btn_limpiar = ttk.Button(btn_frame2, text="Limpiar Campos", 
                                command=self.limpiar_campos)
        btn_limpiar.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        btn_limpiar_resultados = ttk.Button(btn_frame2, text="Limpiar Resultados", 
                                           command=self.limpiar_resultados)
        btn_limpiar_resultados.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        # Consola de resultados
        console_frame = ttk.LabelFrame(main_frame, text="Resultados", padding=5)
        console_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.consola = scrolledtext.ScrolledText(console_frame, wrap=tk.WORD, 
                                               height=10, state='disabled')
        self.consola.pack(fill=tk.BOTH, expand=True)
        
        # Información adicional
        info_frame = ttk.Frame(main_frame)
        info_frame.pack(fill=tk.X, pady=5)
        
        info = ttk.Label(info_frame, 
                        text="• Logaritmo: Requiere valor positivo\n"
                             "• Raíz cuadrada: Requiere valor positivo",
                        justify=tk.LEFT)
        info.pack(anchor=tk.W)
    
    def agregar_salida(self, texto):
        self.consola.config(state='normal')
        self.consola.insert(tk.END, texto + "\n")
        self.consola.see(tk.END)  # Auto-scroll al final
        self.consola.config(state='disabled')
        self.root.update()
    
    def limpiar_campos(self):
        """Limpia el campo de entrada y los resultados"""
        self.entry_valor.delete(0, tk.END)
        self.limpiar_resultados()
    
    def limpiar_resultados(self):
        """Limpia solo el área de resultados"""
        self.consola.config(state='normal')
        self.consola.delete(1.0, tk.END)
        self.consola.config(state='disabled')
    
    def calcular_logaritmo(self):
        try:
            valor_str = self.entry_valor.get().strip()
            if not valor_str:
                raise ValueError("Debe ingresar un valor numérico")
            
            try:
                valor = float(valor_str)
            except ValueError:
                raise ValueError("El valor debe ser numérico para calcular el logaritmo")
            
            if valor < 0:
                raise ArithmeticError("El valor debe ser un número positivo")
            
            resultado = math.log(valor)
            self.agregar_salida(f"Logaritmo neperiano de {valor} = {resultado:.4f}")
            
        except ArithmeticError as e:
            self.agregar_salida(f"Error en logaritmo: {str(e)}")
        except ValueError as e:
            self.agregar_salida(f"Error en logaritmo: {str(e)}")
        except Exception as e:
            self.agregar_salida(f"Error inesperado: {str(e)}")
    
    def calcular_raiz(self):
        try:
            valor_str = self.entry_valor.get().strip()
            if not valor_str:
                raise ValueError("Debe ingresar un valor numérico")
            
            try:
                valor = float(valor_str)
            except ValueError:
                raise ValueError("El valor debe ser numérico para calcular la raíz cuadrada")
            
            if valor < 0:
                raise ArithmeticError("El valor debe ser un número positivo")
            
            resultado = math.sqrt(valor)
            self.agregar_salida(f"Raíz cuadrada de {valor} = {resultado:.4f}")
            
        except ArithmeticError as e:
            self.agregar_salida(f"Error en raíz cuadrada: {str(e)}")
        except ValueError as e:
            self.agregar_salida(f"Error en raíz cuadrada: {str(e)}")
        except Exception as e:
            self.agregar_salida(f"Error inesperado: {str(e)}")


