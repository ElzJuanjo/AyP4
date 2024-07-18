import random
import timeit

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(valor, self.raiz)

    def _insertar(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(valor)
            else:
                self._insertar(valor, nodo_actual.izquierdo)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(valor)
            else:
                self._insertar(valor, nodo_actual.derecho)

    def buscar(self, valor):
        return self._buscar(valor, self.raiz)

    def _buscar(self, valor, nodo_actual):
        if nodo_actual is None:
            return False
        elif valor == nodo_actual.valor:
            return True
        elif valor < nodo_actual.valor:
            return self._buscar(valor, nodo_actual.izquierdo)
        else:
            return self._buscar(valor, nodo_actual.derecho)

def busquedaBinaria(lista, item):
    i = 0
    d = len(lista)-1
    while i <= d:
        medio = (i + d) // 2
        if lista[medio] == item:
            index = lista.index(item)
            print(f"¡El elemento {item} se encuentra en el arreglo! [{index}]")
            return
        elif item < lista[medio]:
            d = medio - 1
        else:
            i = medio + 1
    
    print(f"El elemento {item} NO se encuentra en el arreglo.")

lista = random.sample(range(1, 10000), 998)
copiaLista = lista.copy()
lista.sort()
arbol = ArbolBinario()
for item in copiaLista:
    arbol.insertar(item)

opcion = -1
while opcion != 0:
    print("\n1. Árbol binario de búsqueda\n2. Búsqueda binaria en vector\n0. Salir")
    try:
        opcion = int(input("Ingrese la opción: "))
        valor = int(input("Número a buscar: "))
        if opcion == 1:
            resultado = []
            tiempo = format(timeit.timeit(lambda: resultado.append(arbol.buscar(valor)), number=1),'.20f')
            encontrado = resultado.pop()
            if encontrado:
                print(f"¡El elemento {valor} se encuentra en el árbol!")
            else:
                print(f"El elemento {valor} NO se encuentra en el árbol.")
            print(f"Tiempo: {tiempo}")
        elif opcion == 2:
            tiempo = format(timeit.timeit(lambda: busquedaBinaria(lista, valor), number=1), '.20f')
            print(f"Tiempo: {tiempo}")
    except:
        print("¡Debes ingresar un número entero!")