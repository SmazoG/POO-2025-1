import tkinter as tk
from tkinter import ttk, scrolledtext

class PruebaExcepcionesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Prueba de Excepciones")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        self.crear_interfaz()
        self.limpiar_consola()
    
    def crear_interfaz(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        titulo = ttk.Label(main_frame, text="Prueba de Manejo de Excepciones", 
                          font=("Arial", 14, "bold"))
        titulo.pack(pady=10)
        
        # Descripción
        descripcion = ttk.Label(main_frame, text="Seleccione un bloque de código para ejecutar y ver cómo se manejan las excepciones:",
                               wraplength=450, justify=tk.LEFT)
        descripcion.pack(pady=5)
        
        # Botones
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=10, fill=tk.X)
        
        btn_bloque1 = ttk.Button(btn_frame, text="Ejecutar Primer Bloque Try", 
                                command=self.ejecutar_primer_bloque)
        btn_bloque1.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        btn_bloque2 = ttk.Button(btn_frame, text="Ejecutar Segundo Bloque Try", 
                                command=self.ejecutar_segundo_bloque)
        btn_bloque2.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        btn_limpiar = ttk.Button(btn_frame, text="Limpiar Consola", 
                                command=self.limpiar_consola)
        btn_limpiar.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        # Consola de salida
        console_frame = ttk.LabelFrame(main_frame, text="Salida de Ejecución", padding=5)
        console_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.consola = scrolledtext.ScrolledText(console_frame, wrap=tk.WORD, 
                                               height=10, state='disabled')
        self.consola.pack(fill=tk.BOTH, expand=True)
        
        # Información
        info_frame = ttk.Frame(main_frame)
        info_frame.pack(fill=tk.X, pady=5)
        
        info = ttk.Label(info_frame, text="• Primer Bloque: Genera ArithmeticException (división por cero)\n"
                                        "• Segundo Bloque: Genera NullPointerException (objeto nulo)",
                        justify=tk.LEFT)
        info.pack(anchor=tk.W)
    
    def limpiar_consola(self):
        self.consola.config(state='normal')
        self.consola.delete(1.0, tk.END)
        self.consola.config(state='disabled')
    
    def agregar_salida(self, texto):
        self.consola.config(state='normal')
        self.consola.insert(tk.END, texto + "\n")
        self.consola.see(tk.END)  # Auto-scroll al final
        self.consola.config(state='disabled')
        self.root.update()  # Actualizar la interfaz
    
    def ejecutar_primer_bloque(self):
        self.agregar_salida("\n=== EJECUTANDO PRIMER BLOQUE TRY ===")
        try:
            self.agregar_salida("Ingresando al primer try")
            cociente = 10000 / 0  # Se lanza una excepción
            self.agregar_salida("Después de la división")  # Nunca se ejecuta
        except ZeroDivisionError:
            self.agregar_salida("División por cero")
        finally:
            self.agregar_salida("Ingresando al primer finally")
    
    def ejecutar_segundo_bloque(self):
        self.agregar_salida("\n=== EJECUTANDO SEGUNDO BLOQUE TRY ===")
        try:
            self.agregar_salida("Ingresando al segundo try")
            objeto = None
            objeto.toString()  # Se lanza una excepción
            self.agregar_salida("Imprimiendo objeto")  # Nunca se ejecuta
        except ZeroDivisionError:
            self.agregar_salida("División por cero")
        except Exception as e:
            self.agregar_salida(f"Ocurrió una excepción: {type(e).__name__}")
        finally:
            self.agregar_salida("Ingresando al segundo finally")


