import tkinter as tk
from tkinter import ttk, messagebox
from Bloc import Bloc
from Funciones import ExpresionRegular

class Gestor(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.bloc = Bloc(root)
        self.root = root
        self.login = False
        self.expresion = ExpresionRegular()
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.contenedorDatos()
        self.contenedorRecuperar()
        self.contenedorModificar()
        self.contenedorIngreso()
        
    def contenedorDatos(self):
        contenedor = tk.Frame(self)
        contenedor.grid(row=0, column=0)
        
        self.labelDocumento = tk.Label(contenedor, text="Documento:")
        self.labelDocumento.config(font=("Arial",12,"bold"))
        self.labelDocumento.grid(row=0, column=0)
        
        self.varDocumento = tk.StringVar()
        self.cuadroDocumento = tk.Entry(contenedor, textvariable=self.varDocumento, width=40)
        self.cuadroDocumento.config(bd=5, relief="ridge", background="#606060", font=("Arial", 12))
        self.cuadroDocumento.grid(row=1, column=0)
        
        self.labelCorreo = tk.Label(contenedor, text="Correo:")
        self.labelCorreo.config(font=("Arial",12,"bold"))
        self.labelCorreo.grid(row=2, column=0)
        
        self.varCorreo = tk.StringVar()
        self.cuadroCorreo = tk.Entry(contenedor, textvariable=self.varCorreo, width=40)
        self.cuadroCorreo.config(bd=5, relief="ridge", background="#606060", font=("Arial", 12))
        self.cuadroCorreo.grid(row=3, column=0)
    
    def contenedorRecuperar(self):
        separador = ttk.Separator(self, orient="horizontal")
        separador.grid(row=1, column=0, sticky="ew")
        
        self.botonRecuperar = tk.Button(self, text="Recuperar Clave", command=self.recuperarClave)
        self.botonRecuperar.config(relief="raised", bd=5, bg="#d35631", font=("Arial", 10, "bold"))
        self.botonRecuperar.grid(row=2, column=0)
        
        separador = ttk.Separator(self, orient="horizontal")
        separador.grid(row=3, column=0, sticky="ew")

    def contenedorModificar(self):
        contenedor = tk.Frame(self)
        contenedor.grid(row=4, column=0)
        
        self.labelClaveUno = tk.Label(contenedor, text="Contraseña Actual:")
        self.labelClaveUno.config(font=("Arial",12,"bold"))
        self.labelClaveUno.grid(row=0, column=0)
        
        self.varClaveUno = tk.StringVar()
        self.cuadroClaveUno = tk.Entry(contenedor, textvariable=self.varClaveUno, width=40)
        self.cuadroClaveUno.config(bd=5, relief="ridge", background="#606060", font=("Arial", 12))
        self.cuadroClaveUno.grid(row=1, column=0)

        self.labelClaveDos = tk.Label(contenedor, text="Contraseña Nueva:")
        self.labelClaveDos.config(font=("Arial",12,"bold"))
        self.labelClaveDos.grid(row=2, column=0)
        
        self.varClaveDos = tk.StringVar()
        self.cuadroClaveDos = tk.Entry(contenedor, textvariable=self.varClaveDos, width=40)
        self.cuadroClaveDos.config(bd=5, relief="ridge", background="#606060", font=("Arial", 12))
        self.cuadroClaveDos.grid(row=3, column=0)
        
        self.botonModificar = tk.Button(contenedor, text="Modificar Clave", command=self.modificarClave)
        self.botonModificar.config(relief="raised", bd=5, bg="#d35631", font=("Arial", 10, "bold"))
        self.botonModificar.grid(row=4, column=0, pady=10)

        separador = ttk.Separator(self, orient="horizontal")
        separador.grid(row=5, column=0, sticky="ew")
        
    def contenedorIngreso(self):
        contenedor = tk.Frame(self)
        contenedor.grid(row=6, column=0)
        
        self.botonIngreso = tk.Button(contenedor, text="Ingresar", command=self.ingresarSistema)
        self.botonIngreso.config(relief="raised", bd=5, bg="#d35631", font=("Arial", 10, "bold"))
        self.botonIngreso.grid(row=0, column=0, padx=100)        
        
        self.botonCerrar = tk.Button(contenedor, text="Cerrar Sesión", command=self.cerrarSesion)
        self.botonCerrar.config(relief="raised", bd=5, bg="#d35631", font=("Arial", 10, "bold"), state="disabled")
        self.botonCerrar.grid(row=0, column=1, padx=100)         
    
    def recuperarClave(self):
        if self.bloc.arbolB:
            correo = self.varCorreo.get().strip()
            documento = self.varDocumento.get().strip()
            index = 0
            flag = False
            for i,usuario in enumerate(self.bloc.datos):
                if usuario[1] == documento and usuario[6] == correo:
                    index = i
                    flag = True
                    break
            if flag:
                nodo = self.bloc.arbolB.buscar(index)
                messagebox.showinfo('¡Se ha encontrado!',f'Su clave es: {nodo.clave}')
            else:
                messagebox.showinfo('¡No se pudo validar!', 'Verifique los datos ingresados.')
    
    def modificarClave(self):
        if self.bloc.arbolB:
            correo = self.varCorreo.get().strip()
            documento = self.varDocumento.get().strip()
            claveUno = self.varClaveUno.get().strip()
            claveDos = self.varClaveDos.get().strip()
            
            index = 0
            flag = False
            for i,usuario in enumerate(self.bloc.datos):
                if usuario[1] == documento and usuario[6] == correo:
                    index = i
                    flag = True
                    break
            if flag:
                nodo = self.bloc.arbolB.buscar(index)
                claveActual = nodo.clave
                if claveUno == claveActual:
                    if self.expresion.validarClave(claveDos):
                        self.bloc.arbolB.modificarClave(nodo.valor,claveDos)
                        messagebox.showinfo('¡Se ha cambiado!',f'Nueva clave: {claveDos}')
                    else:
                        messagebox.showinfo('¡Contraseña insegura!','Debe tener al menos:\nUna minúscula.\nUna mayúscula.\nUn carácter especial.\nUn número.\n8 digitos.')
                else:
                    messagebox.showinfo('¡No se pudo validar!', 'Verifique los datos ingresados.')
            else:
                messagebox.showinfo('¡No se pudo validar!', 'Verifique los datos ingresados.')
    
    def ingresarSistema(self):
        if not self.login and self.bloc.arbolB:
            correo = self.varCorreo.get().strip()
            claveUno = self.varClaveUno.get().strip()

            index = 0
            flag = False
            for i,usuario in enumerate(self.bloc.datos):
                if usuario[6] == correo:
                    index = i
                    flag = True
                    break     
                
            if flag:
                nodo = self.bloc.arbolB.buscar(index)
                if claveUno == nodo.clave:     
                    self.root.add(self.bloc.usuarios, text='USUARIOS')
                    self.login = True
                    self.botonCerrar.config(state="normal")
                    self.botonIngreso.config(state="disabled")
                    
                    self.nombre = self.bloc.datos[index][2]
                    self.correo = self.bloc.datos[index][6]
                    if self.expresion.validarPoli(self.correo):
                        messagebox.showinfo('¡Ha iniciado sesión!', f'Bienvenid@ | {self.nombre} [Estudiante]')
                    else:
                        messagebox.showinfo('¡Ha iniciado sesión!', f'Bienvenid@ | {self.nombre}')
                else:
                    messagebox.showinfo('¡No se pudo validar!', 'Verifique los datos ingresados.')
            else:
                messagebox.showinfo('¡No se pudo validar!', 'Verifique los datos ingresados.')
        
    def cerrarSesion(self):
        if self.login and self.bloc.arbolB:
            self.root.hide(2)
            self.login = False
            self.botonIngreso.config(state="normal")
            self.botonCerrar.config(state="disabled")
            if self.expresion.validarPoli(self.correo):
                messagebox.showinfo('¡Sesión cerrada!', f'Hasta luego | {self.nombre} [Estudiante]')
            else:
                messagebox.showinfo('¡Sesión cerrada!', f'Hasta luego | {self.nombre}')