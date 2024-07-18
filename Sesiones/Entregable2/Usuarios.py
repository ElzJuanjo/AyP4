import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import networkx as nx

class Usuarios(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.columnconfigure(0,weight=1)
        
        self.tablaDatos = ttk.Treeview(self, show="headings")
        self.tablaDatos.config(height=15)
        self.tablaDatos.config(columns=("TD", "ID", "NOMBRE", "TOKEN","FN","CIUDAD","CORREO"))
        self.tablaDatos.heading("TD", text="TD")
        self.tablaDatos.heading("ID", text="ID")
        self.tablaDatos.heading("NOMBRE", text="NOMBRE")
        self.tablaDatos.heading("TOKEN", text="TOKEN")
        self.tablaDatos.heading("FN", text="FN")
        self.tablaDatos.heading("CIUDAD", text="CIUDAD")
        self.tablaDatos.heading("CORREO", text="CORREO")
        self.tablaDatos.grid(row=0, column=0)
        
        self.scrollTabla = tk.Scrollbar(self,command=self.tablaDatos.yview)
        self.scrollTabla.grid(row=0, column=1, padx=5, pady=5, sticky="ns")
        self.tablaDatos.config(yscrollcommand=self.scrollTabla.set)     
        
        self.preorden = None
        self.inorden = None
        
        self.botonArbol = tk.Button(self, text="Mostrar Arbol", command=self.mostrarArbol)
        self.botonArbol.config(relief="raised", bd=5, bg="#d35631", font=("Arial", 10, "bold"))
        self.botonArbol.grid(row=1, column=0, pady=10, columnspan=2)
        
    def actualizarValores(self, datos):
        self.tablaDatos.delete(*self.tablaDatos.get_children())
        for dato in datos:
            self.tablaDatos.insert('', 'end', values=dato)
            
    def mostrarArbol(self):
        if self.preorden and self.inorden:
            graficar_arbol(self.inorden, self.preorden)
        else:
            messagebox.showwarning('AVISO', '¡No hay datos de usuarios!')
            
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        
def construir_arbol(inorden, preorden):
    if not inorden or not preorden:
        return None
    
    # El primer elemento de preorden es la raíz
    raiz_valor = preorden.pop(0)
    raiz = Nodo(raiz_valor)
    
    # Encuentra el índice de la raíz en inorden
    indice_raiz = inorden.index(raiz_valor)
    
    # Construye el subárbol izquierdo y derecho recursivamente
    raiz.izquierda = construir_arbol(inorden[:indice_raiz], preorden)
    raiz.derecha = construir_arbol(inorden[indice_raiz+1:], preorden)
    
    return raiz

# Función para agregar nodos y aristas a un grafo de NetworkX
def agregar_nodos_y_aristas(g, nodo, pos={}, x=0, y=0, layer=1):
    if nodo is not None:
        g.add_node(nodo.valor, pos=(x, y))
        if nodo.izquierda:
            g.add_edge(nodo.valor, nodo.izquierda.valor)
            pos = agregar_nodos_y_aristas(g, nodo.izquierda, pos, x - 1/layer, y - 1, layer + 1)
        if nodo.derecha:
            g.add_edge(nodo.valor, nodo.derecha.valor)
            pos = agregar_nodos_y_aristas(g, nodo.derecha, pos, x + 1/layer, y - 1, layer + 1)
    return pos

# Función para graficar el árbol binario
def graficar_arbol(inorden, preorden):
    # Construir el árbol binario
    arbol = construir_arbol(inorden, preorden.copy())
    
    # Crear un grafo de NetworkX
    g = nx.DiGraph()
    
    # Agregar nodos y aristas al grafo
    pos = agregar_nodos_y_aristas(g, arbol)
    
    # Obtener las posiciones de los nodos
    pos = nx.get_node_attributes(g, 'pos')
    
    # Dibujar el grafo
    plt.figure(figsize=(10, 6))
    nx.draw(g, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=12, font_weight='bold', arrows=False)
    plt.show()