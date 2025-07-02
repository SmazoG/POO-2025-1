import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from EquipoMaratonProgramacion import *
from Programador import *

class EquipoMaratonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Equipos de Maratón")
        self.root.geometry("750x580")  # Ventana un poco más ancha
        self.root.resizable(False, False)
        
        self.equipo = None
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Frame principal con scroll
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Canvas para permitir scroll
        canvas = tk.Canvas(main_frame)
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Título
        titulo = ttk.Label(scrollable_frame, text="Gestión de Equipo de Maratón de Programación", 
                          font=("Arial", 14, "bold"))
        titulo.pack(pady=15, padx=20)
        
        # Creación del equipo - Diseño mejorado
        equipo_frame = ttk.LabelFrame(scrollable_frame, text="Datos del Equipo", padding=15)
        equipo_frame.pack(fill=tk.X, padx=20, pady=10)
        
        # Configuración de columnas para mejor distribución
        equipo_frame.columnconfigure(1, weight=1)
        
        campos_equipo = [
            ("Nombre del Equipo:", "nombre_equipo"),
            ("Universidad:", "universidad"),
            ("Lenguaje:", "lenguaje")
        ]
        
        self.entries_equipo = {}
        for i, (label, field) in enumerate(campos_equipo):
            # Etiqueta con ancho fijo para alineación
            lbl = ttk.Label(equipo_frame, text=label, width=22, anchor="e")
            lbl.grid(row=i, column=0, padx=5, pady=7, sticky="e")
            
            # Campo de entrada con padding adicional
            entry = ttk.Entry(equipo_frame, width=35)
            entry.grid(row=i, column=1, padx=5, pady=7, sticky="we")
            self.entries_equipo[field] = entry
        
        # Botón centrado
        btn_frame = ttk.Frame(equipo_frame)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=10)
        
        btn_crear_equipo = ttk.Button(btn_frame, text="Crear Equipo", 
                                     command=self.crear_equipo)
        btn_crear_equipo.pack(pady=5)
        
        # Separador
        ttk.Separator(scrollable_frame, orient='horizontal').pack(fill='x', padx=20, pady=15)
        
        # Añadir programadores - Diseño mejorado
        programadores_frame = ttk.LabelFrame(scrollable_frame, text="Añadir Programadores", padding=15)
        programadores_frame.pack(fill=tk.X, padx=20, pady=10)
        
        # Configuración de columnas
        programadores_frame.columnconfigure(1, weight=1)
        
        campos_programador = [
            ("Nombre:", "nombre_programador"),
            ("Apellidos:", "apellidos_programador")
        ]
        
        self.entries_programador = {}
        for i, (label, field) in enumerate(campos_programador):
            # Etiqueta con ancho fijo para alineación
            lbl = ttk.Label(programadores_frame, text=label, width=22, anchor="e")
            lbl.grid(row=i, column=0, padx=5, pady=7, sticky="e")
            
            # Campo de entrada con padding adicional
            entry = ttk.Entry(programadores_frame, width=35)
            entry.grid(row=i, column=1, padx=5, pady=7, sticky="we")
            self.entries_programador[field] = entry
        
        # Botón centrado
        btn_frame2 = ttk.Frame(programadores_frame)
        btn_frame2.grid(row=2, column=0, columnspan=2, pady=10)
        
        btn_añadir = ttk.Button(btn_frame2, text="Añadir Programador", 
                               command=self.añadir_programador)
        btn_añadir.pack(pady=5)
        
        # Información del equipo
        info_frame = ttk.LabelFrame(scrollable_frame, text="Información del Equipo", padding=10)
        info_frame.pack(fill=tk.BOTH, padx=20, pady=10, expand=True)
        
        self.info_text = scrolledtext.ScrolledText(info_frame, wrap=tk.WORD, height=10,
                                                 font=("Arial", 10))
        self.info_text.pack(fill=tk.BOTH, expand=True)
        self.info_text.config(state='disabled')
        
        # Botones adicionales
        btn_frame = ttk.Frame(scrollable_frame)
        btn_frame.pack(fill=tk.X, padx=20, pady=15)
        
        btn_limpiar = ttk.Button(btn_frame, text="Limpiar Todo", 
                                command=self.limpiar_todo)
        btn_limpiar.pack(side=tk.LEFT, padx=10, ipadx=10)
        
        btn_salir = ttk.Button(btn_frame, text="Salir", 
                              command=self.root.destroy)
        btn_salir.pack(side=tk.RIGHT, padx=10, ipadx=10)
    
    def actualizar_info(self):
        self.info_text.config(state='normal')
        self.info_text.delete(1.0, tk.END)
        
        if self.equipo:
            self.info_text.insert(tk.END, f"Nombre del Equipo: {self.equipo.nombre_equipo}\n")
            self.info_text.insert(tk.END, f"Universidad: {self.equipo.universidad}\n")
            self.info_text.insert(tk.END, f"Lenguaje: {self.equipo.lenguaje_programacion}\n")
            self.info_text.insert(tk.END, f"Programadores ({self.equipo.tamaño_equipo}/3):\n")
            
            for i, prog in enumerate(self.equipo.listar_programadores(), 1):
                self.info_text.insert(tk.END, f"  {i}. {prog}\n")
            
            if self.equipo.esta_lleno():
                self.info_text.insert(tk.END, "\n¡EQUIPO COMPLETO!")
        else:
            self.info_text.insert(tk.END, "No se ha creado ningún equipo.\n"
                                          "Complete los datos del equipo y haga clic en 'Crear Equipo'.")
        
        self.info_text.config(state='disabled')
    
    def crear_equipo(self):
        try:
            nombre = self.entries_equipo['nombre_equipo'].get().strip()
            universidad = self.entries_equipo['universidad'].get().strip()
            lenguaje = self.entries_equipo['lenguaje'].get().strip()
            
            if not nombre or not universidad or not lenguaje:
                raise ValueError("Todos los campos del equipo son obligatorios")
            
            # Validar campos del equipo
            EquipoMaratonProgramacion.validar_campo(nombre)
            EquipoMaratonProgramacion.validar_campo(universidad)
            EquipoMaratonProgramacion.validar_campo(lenguaje)
            
            self.equipo = EquipoMaratonProgramacion(nombre, universidad, lenguaje)
            self.actualizar_info()
            messagebox.showinfo("Equipo Creado", "Equipo creado exitosamente.\nAhora puede añadir programadores.")
        
        except Exception as e:
            messagebox.showerror("Error al crear equipo", str(e))
    
    def añadir_programador(self):
        if not self.equipo:
            messagebox.showerror("Error", "Primero debe crear un equipo.")
            return
        
        try:
            nombre = self.entries_programador['nombre_programador'].get().strip()
            apellidos = self.entries_programador['apellidos_programador'].get().strip()
            
            if not nombre or not apellidos:
                raise ValueError("Debe completar ambos campos del programador")
            
            # Validar campos del programador
            EquipoMaratonProgramacion.validar_campo(nombre)
            EquipoMaratonProgramacion.validar_campo(apellidos)
            
            programador = Programador(nombre, apellidos)
            self.equipo.añadir_programador(programador)
            
            # Limpiar campos y actualizar info
            self.entries_programador['nombre_programador'].delete(0, tk.END)
            self.entries_programador['apellidos_programador'].delete(0, tk.END)
            self.actualizar_info()
            
            if self.equipo.esta_lleno():
                messagebox.showinfo("Equipo Completo", "¡El equipo está completo con 3 programadores!")
        
        except Exception as e:
            messagebox.showerror("Error al añadir programador", str(e))
    
    def limpiar_todo(self):
        # Limpiar campos
        for entry in self.entries_equipo.values():
            entry.delete(0, tk.END)
        
        for entry in self.entries_programador.values():
            entry.delete(0, tk.END)
        
        # Resetear equipo
        self.equipo = None
        
        # Actualizar información
        self.actualizar_info()
        
        messagebox.showinfo("Limpiar", "Todos los campos han sido limpiados y el equipo ha sido eliminado.")

