import time
import random
#lista = [2,124,23,5,89,-1,44,643,34]
lista = random.sample(range(1,1001),1000)
def mergeSort(x):
    izquierda = []
    derecha = []
    if (len(x) <= 1):
        return x
    else:
        mediana = int(len(x)/2)
        for i in range(0,mediana):
            izquierda.append(x[i])
        for i in range(mediana,len(x)):
            derecha.append(x[i])
        izquierda = mergeSort(izquierda)
        derecha = mergeSort(derecha)
        ultimoizquierda = len(izquierda)
        if(izquierda[ultimoizquierda-1] <= derecha[0]):
            izquierda.extend(derecha)
            return izquierda
        resultado = merge(izquierda, derecha)
        return resultado


def merge(x, y):
    resultado = []
    while len(x) > 0 and len(y) > 0:
        if(x[0] <= y[0]):
            resultado.append(x[0])
            del x[0]
        else:
            resultado.append(y[0])
            del y[0]
    if(len(x)>0):
        resultado.extend(x)
    if(len(y)>0):
        resultado.extend(y)
    return resultado
inicio = time.time()
resultado = mergeSort(lista)
fin = time.time()
#print(resultado)
print(f"Tiempo con MergeSort: {fin-inicio}")
