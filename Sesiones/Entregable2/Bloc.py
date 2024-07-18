import tkinter as tk
from tkinter import filedialog, END, ttk, messagebox
from Funciones import *
from Usuarios import Usuarios

class Bloc(tk.Frame):
    def __init__(self, root=None):
        self.archivoAbierto = None
        self.re = ExpresionRegular()
        self.arbolB = None
        super().__init__(root)
        self.usuarios = Usuarios(root)
        self.opcionesBloc()
        self.columnconfigure(1,weight=1)

    def opcionesBloc(self):
        frameDatos = tk.Frame(self)
        frameDatos.grid(row=0, column=0, padx=5, pady=5)

        botonAbrir = tk.Button(frameDatos, text="Abrir", command=self.abrirArchivo)
        botonAbrir.config(relief="raised", bd=5, bg="#d35631", font=("Arial", 10, "bold"))
        botonAbrir.grid(row=0, column=0, pady=5)

        botonRegistrar = tk.Button(frameDatos, text="Registrar", command=self.registrarUsuarios)
        botonRegistrar.config(relief="raised", bd=5, bg="#d35631", font=("Arial", 10, "bold"))
        botonRegistrar.grid(row=1, column=0, pady=5)

        self.campoDeTexto = tk.Text(self)
        self.campoDeTexto.config(bd=5, relief="ridge",background="#606060", font=("Arial", 12), height=20)
        self.campoDeTexto.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        scrollCampoDeTexto = tk.Scrollbar(self, command=self.campoDeTexto.yview)
        scrollCampoDeTexto.grid(row=0, column=2, padx=5, pady=5, sticky="ns")
        self.campoDeTexto.config(yscrollcommand=scrollCampoDeTexto.set)
        
        separador = ttk.Separator(self, orient="vertical")
        separador.grid(row=0, column=3, sticky="ns")
        
        contenedorRegistro = tk.Frame(self)
        contenedorRegistro.grid(row=0, column=4)
        
        self.labelRegistro = tk.Label(contenedorRegistro, text="REGISTRO")
        self.labelRegistro.config(font=("Arial",14,"bold"))
        self.labelRegistro.grid(row=0, column=0)
        
        self.campoDeRegistro = tk.Text(contenedorRegistro)
        self.campoDeRegistro.config(bd=5,relief="ridge", font=("Arial", 12), width=30)
        self.campoDeRegistro.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.campoDeRegistro.config(state="disabled")
        
        scrollcampoDeRegistro = tk.Scrollbar(contenedorRegistro, command=self.campoDeRegistro.yview)
        scrollcampoDeRegistro.grid(row=1, column=1, padx=5, pady=5, sticky="ns")
        self.campoDeRegistro.config(yscrollcommand=scrollcampoDeRegistro.set)

    def abrirArchivo(self):
        self.archivoAbierto = filedialog.askopenfile(mode='r+')
        if self.archivoAbierto:
            self.campoDeTexto.delete(1.0, END)
            with open(self.archivoAbierto.name, 'r+', encoding="UTF-8") as documento:
                texto = documento.read()
                self.campoDeTexto.insert(1.0, texto)

    def guardarArchivo(self):
        contenido = self.campoDeTexto.get(1.0, END)
        contenido = contenido.strip()
        
        if(len(contenido)>0):
            if self.archivoAbierto:
                with open(self.archivoAbierto.name, 'w', encoding="UTF-8") as documento:
                    texto = self.campoDeTexto.get(1.0, END)
                    documento.write(texto)
            else:
                self.guardarComoArchivo()

    def guardarComoArchivo(self):
        archivo = filedialog.asksaveasfilename(defaultextension='txt',
                                               filetypes=[('Documentos de texto', '*.txt'),
                                                          ('Todos los archivos', '*.*')])
        if archivo:
            with open(archivo, 'w', encoding="UTF-8") as documento:
                texto = self.campoDeTexto.get(1.0, END)
                documento.write(texto)
                self.archivoAbierto = documento
                
    def registrarUsuarios(self):
        self.guardarArchivo()
        try:
            expresion = ExpresionRegular()
            with open(self.archivoAbierto.name, 'r', encoding='utf-8') as documento:
                lineas = documento.readlines()     
                self.datos = []
                contador = 0
                registro = ''
                for i,linea in enumerate(lineas):
                    linea = linea.strip()
                    valores = linea.split(';')
                    guardar = True
                    
                    if(len(valores)==6):
                        for j,valor in enumerate(valores):
                            match j:
                                case 1:
                                    if valores[0] == 'CC':
                                        if not expresion.validarCedula(valor):
                                            registro += f'» El usuario [{i}] no tiene CC númerica.\n\n'
                                            guardar=False
                                            break
                                case 3:
                                    if not expresion.validarFecha(valor):
                                        registro += f'» El usuario [{i}] no tiene fecha en formato dd/mm/aaaa.\n\n'
                                        guardar=False
                                        break
                                        
                                case 5:
                                    if expresion.validarPoli(valor):
                                        registro += f'» ¡El usuario [{i}] tiene un correo institucional!\n\n'
                                    elif not expresion.validarCorreo(valor):
                                        registro += f'»El usuario [{i}] no tiene un correo válido.\n\n'
                                        guardar=False
                                        break     
                    else:
                        guardar=False  
                    
                    if(guardar): 
                        contador+=1         
                        self.datos.append(valores)
            
            if(len(self.datos)>0):
                archivo = filedialog.asksaveasfilename(defaultextension='txt',
                                                    filetypes=[('Documentos de texto', '*.txt'),
                                                                ('Todos los archivos', '*.*')])
            
            if archivo:
                self.campoDeRegistro.config(state="normal")
                self.campoDeRegistro.delete(1.0, END)
                self.campoDeRegistro.insert(1.0, registro)
                self.campoDeRegistro.config(state="disabled")
                            
                claves = expresion.listaClaves(contador)     
                hash = Hashing(claves)
                tokens = hash.crearHashTableSHA1()
                
                texto = ''
                
                self.arbolB = ArbolBinario()
                
                for i,clave in enumerate(claves):
                    texto += f"{i};{clave}\n"
                    self.arbolB.insertar(i,clave)
                    
                self.usuarios.preorden = self.arbolB.recorrido_preorden()
                self.usuarios.inorden = self.arbolB.recorrido_inorden()
                
                with open(archivo, 'w', encoding="UTF-8") as documento:
                        documento.write(texto)
                    
                for i, token in enumerate(tokens):
                    self.datos[i].insert(3, token)
                
                self.usuarios.actualizarValores(self.datos)
            else:
                messagebox.showwarning('AVISO','¡Debe guardar el archivo con las claves!')
        except:
            pass