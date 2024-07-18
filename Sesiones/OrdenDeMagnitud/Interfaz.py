import tkinter as tk
from tkinter import filedialog, END, messagebox, simpledialog
import sv_ttk
import numpy as np
import time
import timeit

class Interfaz:
    def __init__(self):
        self.archivo = None
        
        self.ventana = tk.Tk()
        self.ventana.title("Juan José JV [AyP4]")
        self.ventana.resizable(False,False)
        
        self.botonLeer = tk.Button(self.ventana, text="LEER matriz", command=self.leermatriz)
        self.botonLeer.config(relief="raised", bd=5, bg="#008080", font=("Cascadia Code", 10, "bold"))
        self.botonLeer.grid(row=0, column=0, pady=20)
        
        self.botonN = tk.Button(self.ventana, text="INGRESAR N", command=self.ingresarN)
        self.botonN.config(relief="raised", bd=5, bg="#008080", font=("Cascadia Code", 10, "bold"))
        self.botonN.grid(row=1, column=0)        
        
        labelRegistro = tk.Label(self.ventana, text="REGISTRO")
        labelRegistro.config(font=("Cascadia Code",14,"bold"))
        labelRegistro.grid(row=2, column=0)
        
        contenedorRegistro = tk.Frame(self.ventana)
        contenedorRegistro.grid(row=3, column=0, pady=20, padx=20)
        
        self.campoRegistro = tk.Text(contenedorRegistro)
        self.campoRegistro.config(bd=5,relief="ridge", font=("Cascadia Code", 12), width=70, height=7 ,state="disabled")
        self.campoRegistro.grid(row=0, column=0)
        
        scrollcampoDeRegistro = tk.Scrollbar(contenedorRegistro, command=self.campoRegistro.yview)
        scrollcampoDeRegistro.grid(row=0, column=1, padx=5, pady=5, sticky="ns")
        self.campoRegistro.config(yscrollcommand=scrollcampoDeRegistro.set)
        
        self.centrarVentana()
        sv_ttk.use_dark_theme()
        self.ventana.mainloop()
        
    def centrarVentana(self):
        self.ventana.update_idletasks()
        x = (self.ventana.winfo_screenwidth() // 2) - (self.ventana.winfo_width() // 2)
        y = (self.ventana.winfo_screenheight() // 2) - (self.ventana.winfo_height() // 2)
        self.ventana.geometry(f'{self.ventana.winfo_width()}x{self.ventana.winfo_height()}+{x}+{y}')
        
    def leermatriz(self):
        self.archivo = filedialog.askopenfile(mode='r+')

        if self.archivo:
            self.matriz = []
            with open(self.archivo.name, 'r', encoding="UTF-8") as documento:
                for linea in documento:
                    fila = list(map(int, linea.strip().split()))
                    self.matriz.append(fila)

            self.matriz = np.array(self.matriz)
        
    def ingresarN(self):
        if self.archivo:
            n = None
            try:
                n = int(simpledialog.askstring("", "Ingrese el valor de n:"))
            except:
                messagebox.showwarning("AVISO","¡Debes ingresar un número entero!")
            
            if n: 
                self.validaciones(n)
        else:
            messagebox.showwarning("AVISO","¡Debes leer la matriz!")
                               
    def validaciones(self, n):
        registro = []

        tiempo = format(timeit.timeit(lambda: registro.append(self.primerPosicion(n)), number=1), '.20f')
        registro.append(f"Tiempo: {tiempo}\n\n")
        
        tiempo = format(timeit.timeit(lambda: registro.append(self.posicionMedio(n)), number=1), '.20f')
        registro.append(f"Tiempo: {tiempo}\n\n")
        
        tiempo = format(timeit.timeit(lambda: registro.append(self.ultimaPosicion(n)), number=1), '.20f')
        registro.append(f"Tiempo: {tiempo}\n\n")
        
        resultado = []
        tiempo = format(timeit.timeit(lambda: resultado.append(self.calcularProbabilidad(n)), number=1), '.20f')
        probabilidad = resultado.pop()               
        registro.append(f"4. La probabilidad de que el valor {n} no esté en ninguna posición de la matriz es del {probabilidad}%\n")
        registro.append(f"Tiempo: {tiempo}")
        
        registro = "".join(registro)
        self.campoRegistro.config(state="normal")
        self.campoRegistro.delete(1.0, END)
        self.campoRegistro.insert(1.0, registro)
        self.campoRegistro.config(state="disabled")
        
    def primerPosicion(self,n):
        if n == self.matriz[0,0]:
            registro = f"1. El número {n} está en la primera posición | [0,0]\n"
        else:
            registro = f"1. El número {n} NO está en la primera posición | [0,0]\n"
        return registro
    
    def posicionMedio(self,n):
        mitad = (len(self.matriz) // 2) -1
        if n == self.matriz[mitad,mitad]:
            registro = f"2. El número {n} está en la posición del medio | [{mitad},{mitad}]\n"
        else:
            registro = f"2. El número {n} NO está en la posición del medio | [{mitad},{mitad}]\n"
        return registro
    
    def ultimaPosicion(self,n):
        ultima = len(self.matriz) - 1
        if n == self.matriz[ultima,ultima]:
            registro = f"3. El número {n} está en la última posición | [{ultima},{ultima}]\n"
        else:
            registro = f"3. El número {n} NO está en la última posición | [{ultima},{ultima}]\n"  
        return registro
        
    def calcularProbabilidad(self, n):
        totalElementos = self.matriz.size
        elementosDiferentes = np.count_nonzero(self.matriz != n)
        probabilidad = (elementosDiferentes / totalElementos) * 100
        return probabilidad