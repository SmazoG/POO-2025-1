import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from Vendedor import *

class VendedorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Vendedores")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        
        self.crear_interfaz()
        self.limpiar_consola()
    
    def crear_interfaz(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding=15)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        titulo = ttk.Label(main_frame, text="Registro de Vendedores", 
                          font=("Arial", 14, "bold"))
        titulo.pack(pady=10)
        
        # Formulario de entrada
        form_frame = ttk.LabelFrame(main_frame, text="Datos del Vendedor", padding=10)
        form_frame.pack(fill=tk.X, pady=10)
        
        # Campos del formulario
        campos = [
            ("Nombre:", "nombre"),
            ("Apellidos:", "apellidos"),
            ("Edad:", "edad")
        ]
        
        self.entries = {}
        for i, (label, field) in enumerate(campos):
            row = ttk.Frame(form_frame)
            row.pack(fill=tk.X, pady=5)
            
            lbl = ttk.Label(row, text=label, width=10)
            lbl.pack(side=tk.LEFT, padx=5)
            
            entry = ttk.Entry(row)
            entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
            
            self.entries[field] = entry
        
        # Botones
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=10, fill=tk.X)
        
        btn_registrar = ttk.Button(btn_frame, text="Registrar Vendedor", 
                                  command=self.registrar_vendedor)
        btn_registrar.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        btn_limpiar = ttk.Button(btn_frame, text="Limpiar Campos", 
                                command=self.limpiar_campos)
        btn_limpiar.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        # Consola de salida
        console_frame = ttk.LabelFrame(main_frame, text="Información del Vendedor", padding=5)
        console_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.consola = scrolledtext.ScrolledText(console_frame, wrap=tk.WORD, 
                                               height=10, state='disabled')
        self.consola.pack(fill=tk.BOTH, expand=True)
        
        # Validaciones
        valid_frame = ttk.Frame(main_frame)
        valid_frame.pack(fill=tk.X, pady=5)
        
        valid_label = ttk.Label(valid_frame, 
                               text="Validaciones: Edad debe ser entre 18 y 120 años",
                               font=("Arial", 9))
        valid_label.pack(anchor=tk.W)
    
    def limpiar_consola(self):
        self.consola.config(state='normal')
        self.consola.delete(1.0, tk.END)
        self.consola.config(state='disabled')
    
    def limpiar_campos(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.limpiar_consola()
    
    def agregar_salida(self, texto):
        self.consola.config(state='normal')
        self.consola.insert(tk.END, texto + "\n")
        self.consola.see(tk.END)
        self.consola.config(state='disabled')
        self.root.update()
    
    def registrar_vendedor(self):
        try:
            # Obtener datos del formulario
            nombre = self.entries['nombre'].get().strip()
            apellidos = self.entries['apellidos'].get().strip()
            edad_str = self.entries['edad'].get().strip()
            
            # Validar campos obligatorios
            if not nombre or not apellidos or not edad_str:
                raise ValueError("Todos los campos son obligatorios")
            
            # Convertir y validar edad
            try:
                edad = int(edad_str)
            except ValueError:
                raise ValueError("La edad debe ser un número entero")
            
            # Crear y validar vendedor
            vendedor = Vendedor(nombre, apellidos)
            vendedor.verificar_edad(edad)
            
            # Mostrar resultados
            self.limpiar_consola()
            self.agregar_salida("=== VENDEDOR REGISTRADO CON ÉXITO ===")
            self.agregar_salida(vendedor.imprimir())
            self.agregar_salida("\n¡Registro completado satisfactoriamente!")
            
        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e))
        except Exception as e:
            messagebox.showerror("Error Inesperado", f"Ocurrió un error: {str(e)}")

