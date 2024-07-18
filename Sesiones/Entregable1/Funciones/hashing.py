# -*- coding: utf-8 -*-
# Medio Cuadrado y SHA1

import hashlib
import time

# SHA1
def hashSHA1(data):
    data = str(data).encode()

    sha1 = hashlib.sha1()

    sha1.update(data)

    return sha1.hexdigest()

def crearHashTableSHA1(datos):
    hashTable = {}

    for dato in datos:
        hashTable[dato] = hashSHA1(dato)

    hashTableInvertida = invertirDiccionario(hashTable)

    return [list(hashTableInvertida.values()),list(hashTable.values())] 
    # Retorna como una lista de dos listas para tener la información en un tipo de dato más compatible con java

def invertirDiccionario(diccionario):
    inverted = {v: k for k, v in diccionario.items()}
    return inverted

def buscarEnHashTable(hashTable,key):
    pos = hashTable[1].index(key)
    return [pos,key,hashTable[0][pos]]

# MEDIO CUADRADO
def hashMedioCuadrado(data):
    digitos = 3
    cuadrado = str(data**2)

    division = len(cuadrado)//2

    key = cuadrado[division-1:division+2]

    return key

def crearHashTableMedioCuadrado(datos):
    valuesTable = []
    keysTable = []

    for dato in datos:
        key = hashMedioCuadrado(dato)
        if key in keysTable:
            int_list = [int(s) for s in keysTable]
            key = min(int_list)
            while str(key) in keysTable:
                key += 1
            key = str(key)
        valuesTable.append(dato)
        keysTable.append(key)

    return [valuesTable,keysTable]

def calculateTimes(datos):
    tiempos = []
    for i in range(2):
        inicio = time.time()
        copiaDatos = list(datos)
        if i==0:
            crearHashTableSHA1(copiaDatos)
        elif i==1:
            crearHashTableMedioCuadrado(copiaDatos)
        fin = time.time()
        tiempos.append(fin - inicio)
    print("\t* TIEMPOS DE HASHING *")
    print("SHA-1: {}".format(tiempos[0]))
    print("Medio Cuadrado: {}".format(tiempos[1]))