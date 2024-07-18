Escribir un algoritmo que lea una matriz (mínimo 1000x1000) de enteros desde un archivo de texto. Dado n por el usuario se debe validar:

1. Si n está en la primera posición
2. Si n está en la posición de la mitad
3. Si n está en la última posición
4. Si n tiene una probabilidad del 60% de no estar en ninguna posición

* Mostrar el tiempo que demora cada caso

**Orden de magnitud para los cuatro casos:** Lineal = O(n) | En el método "validaciones" del archivo Interfaz.py, sólo usamos a n para condicionales, las respectivas posiciones se calculan con funciones de python, al igual que la probabilidad la facilita la libreria de numpy. Por lo que no se presenta complejidad.
