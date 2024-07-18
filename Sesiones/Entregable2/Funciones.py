import re
import random
import string
import hashlib
from tkinter import filedialog, messagebox

class ExpresionRegular:
    def __init__(self):
        self.expresionCedula = r'^\d{5,11}$'
        self.expresionClave =  r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&*()-_+=])[\w@#$%^&*()-+=]{8,}$'
        self.expresionFecha = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{4})$'
        self.expresionPoli =  r'^[a-zA-Z0-9._%+-]+@elpoli\.edu\.co$'
        self.expresionCorreo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
    def validarCedula(self, info):
        return re.search(self.expresionCedula, info)
    
    def validarClave(self, info):
        return re.search(self.expresionClave, info)

    def validarFecha(self, info):
        return re.search(self.expresionFecha, info)

    def validarPoli(self, info):
        return re.search(self.expresionPoli, info)
    
    def validarCorreo(self, info):
        return re.search(self.expresionCorreo, info)
    
    def crearClaves(self):
        minuscula = string.ascii_lowercase
        mayuscula = string.ascii_uppercase
        numeros = string.digits
        caracteres = '@#$%^&*()-_+='
        contenidoClave = minuscula + mayuscula + numeros + caracteres  
        
        while True:
            password = [
                random.choice(minuscula),
                random.choice(mayuscula),
                random.choice(numeros),
                random.choice(caracteres)
            ]
            
            while len(password)<8:
                password.append(random.choice(contenidoClave))
            
            random.shuffle(password)
            password = ''.join(password)
            
            if self.validarClave(password):
                return password
    
    def listaClaves(self, n):
        self.claves = [self.crearClaves() for i in range(n)]     
        return self.claves

class Hashing:
    def __init__(self, claves):
        self.claves = claves
        
    def hashSHA1(self,clave):
        clave = str(clave).encode()
        sha1 = hashlib.sha1()
        sha1.update(clave)
        return sha1.hexdigest()

    def crearHashTableSHA1(self):
        hashTable = {}
        for clave in self.claves:
            hashTable[clave] = self.hashSHA1(clave)
        tokens = list(hashTable.values())
        return tokens

class Nodo:
    def __init__(self, valor, clave):
        self.valor = valor
        self.clave = clave
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor, clave):
        nuevo_nodo = Nodo(valor, clave)
        if not self.raiz:
            self.raiz = nuevo_nodo
            return
        cola = [self.raiz]
        while cola:
            actual = cola.pop(0)
            if not actual.izquierdo:
                actual.izquierdo = nuevo_nodo
                return
            else:
                cola.append(actual.izquierdo)
            if not actual.derecho:
                actual.derecho = nuevo_nodo
                return
            else:
                cola.append(actual.derecho)
                
    def buscar(self, valor):
        if not self.raiz:
            return None
        cola = [self.raiz]
        while cola:
            actual = cola.pop(0)
            if actual.valor == valor:
                return actual
            if actual.izquierdo:
                cola.append(actual.izquierdo)
            if actual.derecho:
                cola.append(actual.derecho)
        return None
    
    def recorrido_inorden(self):
        elementos = []
        self._recorrido_inorden(self.raiz, elementos)
        return elementos

    def _recorrido_inorden(self, nodo_actual, elementos):
        if nodo_actual:
            self._recorrido_inorden(nodo_actual.izquierdo, elementos)
            elementos.append(nodo_actual.valor)
            self._recorrido_inorden(nodo_actual.derecho, elementos)

    def recorrido_preorden(self):
        elementos = []
        self._recorrido_preorden(self.raiz, elementos)
        return elementos

    def _recorrido_preorden(self, nodo_actual, elementos):
        if nodo_actual:
            elementos.append(nodo_actual.valor)
            self._recorrido_preorden(nodo_actual.izquierdo, elementos)
            self._recorrido_preorden(nodo_actual.derecho, elementos)
            
    def guardarDatos(self):
        lista = []
        if not self.raiz:
            return
        cola = [self.raiz]
        while cola:
            actual = cola.pop(0)
            lista.append(f'{actual.valor};{actual.clave}')
            if actual.izquierdo:
                cola.append(actual.izquierdo)
            if actual.derecho:
                cola.append(actual.derecho)
        return lista
    
    def modificarClave(self,index,nuevaClave):
        lineas = self.guardarDatos()
        if 0 <= index < len(lineas):
            lineas[index] = f'{index};{nuevaClave}'
            
        archivo = filedialog.asksaveasfilename(defaultextension='txt',
                                               filetypes=[('Documentos de texto', '*.txt'),
                                                          ('Todos los archivos', '*.*')])
        if archivo:
            texto = ''
            for linea in lineas:
                texto += f'{linea}\n'
            with open(archivo, 'w', encoding="UTF-8") as documento:
                documento.write(texto)
                self.archivoAbierto = documento
            
            pointer = self.buscar(index)
            pointer.clave = nuevaClave
        else:
            messagebox.showwarning('AVISO','¡Debe guardar el archivo con las claves!')