# -*- coding: utf-8 -*-
import timeit

def quickSort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[1]
        
        menores = [x for x in lista[1:] if x<pivote]
        mayores = [x for x in lista[1:] if x>pivote]

        return quickSort(menores) + [pivote] + quickSort(mayores)
    
def countingSort(lista, exp):
    n = len(lista)
    salida = [0] * n    
    contador = [0] * 10

    for i in range(n):
        index = lista[i] // exp
        contador[index % 10] += 1

    for i in range(1, 10):
        contador[i] += contador[i - 1]

    i = n - 1
    while i >= 0:
        index = lista[i] // exp
        salida[contador[index % 10] - 1] = lista[i]
        contador[index % 10] -= 1
        i -= 1

    i = 0
    for i in range(n):
        lista[i] = salida[i]

def radixSort(lista):
    max_element = max(lista)
    exp = 1
    while max_element // exp > 0:
        countingSort(lista, exp)
        exp *= 10
    return lista

def heapify(lista, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and lista[left] > lista[largest]:
        largest = left

    if right < n and lista[right] > lista[largest]:
        largest = right

    if largest != i:
        lista[i], lista[largest] = lista[largest], lista[i]
        heapify(lista, n, largest)

def heapSort(lista):
    n = len(lista)

    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]  
        heapify(lista, i, 0)

    return lista

def shellSort(lista):
    n = len(lista)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = lista[i]
            j = i
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp
        gap //= 2
    return lista

def bucketSort(lista):
    max_val = max(lista)
    min_val = min(lista)
    range_val = max_val - min_val + 1

    num_buckets = len(lista)
    buckets = [[] for _ in range(num_buckets)]

    for num in lista:
        index = (num - min_val) * (num_buckets - 1) // range_val
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    k = 0
    for bucket in buckets:
        for num in bucket:
            lista[k] = num
            k += 1
    
    return lista

def calculateTimes(lista):
    tiempos = []
    for i in range(5):
        copiaLista = list(lista)
        if i==0:
            tiempo = float(format(timeit.timeit(lambda: quickSort(copiaLista), number=1), '.20f'))
        elif i==1:
            tiempo = float(format(timeit.timeit(lambda: heapSort(copiaLista), number=1), '.20f'))
        elif i==2:
            tiempo = float(format(timeit.timeit(lambda: shellSort(copiaLista), number=1), '.20f'))
        elif i==3:
            tiempo = float(format(timeit.timeit(lambda: radixSort(copiaLista), number=1), '.20f'))
        elif i==4:
            tiempo = float(format(timeit.timeit(lambda: bucketSort(copiaLista), number=1), '.20f'))
        tiempos.append(tiempo)
    return tiempos