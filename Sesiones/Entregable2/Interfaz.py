import tkinter as tk
from tkinter import ttk
from Gestor import Gestor
import sv_ttk

class Interfaz:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Juan José JV [AyP4]')
        self.ventana.resizable(False, False)
        
        self.navegacion = ttk.Notebook(self.ventana)
        self.navegacion.pack(fill="both")
        self.gestor = Gestor(self.navegacion)
        self.navegacion.add(self.gestor, text='SISTEMA')
        self.navegacion.add(self.gestor.bloc, text='EDITOR')
        self.navegacion.add(self.gestor.bloc.usuarios, text='USUARIOS')      
        self.navegacion.hide(2)
        
        sv_ttk.use_dark_theme()
        self.centrarVentana()
        self.ventana.mainloop()
        
    def centrarVentana(self):
        self.ventana.update_idletasks()
        x = (self.ventana.winfo_screenwidth() // 2) - (self.ventana.winfo_width() // 2)
        y = (self.ventana.winfo_screenheight() // 2) - (self.ventana.winfo_height() // 2)
        self.ventana.geometry(f'{self.ventana.winfo_width()}x{self.ventana.winfo_height()}+{x}+{y}')

if __name__ == "__main__":
    app = Interfaz()