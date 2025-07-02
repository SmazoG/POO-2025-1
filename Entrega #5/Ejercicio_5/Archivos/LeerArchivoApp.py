import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import os

class LeerArchivoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lector de Archivos de Texto")
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        
        # Configurar icono (si está disponible)
        try:
            self.root.iconbitmap("icono.ico")
        except:
            pass
        
        self.crear_interfaz()
        self.archivo_actual = ""
    
    def crear_interfaz(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding=15)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Barra de herramientas superior
        toolbar_frame = ttk.Frame(main_frame)
        toolbar_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Botones de acción
        btn_abrir = ttk.Button(toolbar_frame, text="Abrir Archivo", 
                              command=self.abrir_archivo)
        btn_abrir.pack(side=tk.LEFT, padx=5)
        
        btn_guardar = ttk.Button(toolbar_frame, text="Guardar", 
                                command=self.guardar_archivo, state="disabled")
        btn_guardar.pack(side=tk.LEFT, padx=5)
        self.btn_guardar = btn_guardar
        
        btn_limpiar = ttk.Button(toolbar_frame, text="Limpiar", 
                                command=self.limpiar_contenido)
        btn_limpiar.pack(side=tk.LEFT, padx=5)
        
        # Separador
        ttk.Separator(toolbar_frame, orient='vertical').pack(side=tk.LEFT, padx=10, fill=tk.Y)
        
        # Etiqueta de información
        self.estado_label = ttk.Label(toolbar_frame, text="No hay archivo abierto")
        self.estado_label.pack(side=tk.LEFT, padx=5)
        
        # Frame para ruta de archivo
        ruta_frame = ttk.Frame(main_frame)
        ruta_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(ruta_frame, text="Ruta del archivo:").pack(side=tk.LEFT, padx=(0, 5))
        
        self.ruta_entry = ttk.Entry(ruta_frame)
        self.ruta_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        btn_explorar = ttk.Button(ruta_frame, text="Explorar", 
                                 command=self.explorar_archivo)
        btn_explorar.pack(side=tk.LEFT)
        
        # Área de contenido
        contenido_frame = ttk.LabelFrame(main_frame, text="Contenido del archivo", padding=5)
        contenido_frame.pack(fill=tk.BOTH, expand=True)
        
        self.contenido_text = scrolledtext.ScrolledText(contenido_frame, wrap=tk.WORD,
                                                      font=("Consolas", 10))
        self.contenido_text.pack(fill=tk.BOTH, expand=True)
        self.contenido_text.config(state='disabled')
        
        # Barra de estado inferior
        status_frame = ttk.Frame(main_frame)
        status_frame.pack(fill=tk.X, pady=(10, 0))
        
        self.status_label = ttk.Label(status_frame, text="Listo")
        self.status_label.pack(side=tk.LEFT)
        
        # Asignar evento para habilitar edición
        self.contenido_text.bind("<Button-1>", self.habilitar_edicion)
    
    def habilitar_edicion(self, event):
        self.contenido_text.config(state='normal')
        self.btn_guardar.config(state="normal")
        self.status_label.config(text="Modo edición activado - Recuerde guardar los cambios")
    
    def actualizar_estado(self, mensaje):
        self.estado_label.config(text=mensaje)
        self.status_label.config(text=mensaje)
    
    def abrir_archivo(self):
        try:
            filepath = filedialog.askopenfilename(
                title="Seleccionar archivo de texto",
                filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
            )
            
            if not filepath:
                return
                
            self.archivo_actual = filepath
            self.ruta_entry.delete(0, tk.END)
            self.ruta_entry.insert(0, filepath)
            
            self.actualizar_estado(f"Leyendo: {os.path.basename(filepath)}")
            
            # Leer contenido del archivo
            with open(filepath, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
            
            # Mostrar contenido
            self.contenido_text.config(state='normal')
            self.contenido_text.delete(1.0, tk.END)
            self.contenido_text.insert(tk.END, contenido)
            self.contenido_text.config(state='disabled')
            self.btn_guardar.config(state="disabled")
            
            self.actualizar_estado(f"Archivo cargado: {os.path.basename(filepath)} - {len(contenido)} caracteres")
            
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer el archivo:\n{str(e)}")
            self.actualizar_estado("Error al leer el archivo")
    
    def explorar_archivo(self):
        self.abrir_archivo()
    
    def guardar_archivo(self):
        if not self.archivo_actual:
            messagebox.showwarning("Guardar", "No hay archivo abierto para guardar")
            return
            
        try:
            contenido = self.contenido_text.get(1.0, tk.END)
            
            with open(self.archivo_actual, 'w', encoding='utf-8') as archivo:
                archivo.write(contenido)
            
            self.contenido_text.config(state='disabled')
            self.btn_guardar.config(state="disabled")
            self.actualizar_estado(f"Archivo guardado: {os.path.basename(self.archivo_actual)}")
            
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{str(e)}")
            self.actualizar_estado("Error al guardar el archivo")
    
    def limpiar_contenido(self):
        self.ruta_entry.delete(0, tk.END)
        self.contenido_text.config(state='normal')
        self.contenido_text.delete(1.0, tk.END)
        self.contenido_text.config(state='disabled')
        self.archivo_actual = ""
        self.btn_guardar.config(state="disabled")
        self.actualizar_estado("No hay archivo abierto")

