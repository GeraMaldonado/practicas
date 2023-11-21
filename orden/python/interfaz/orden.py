import matplotlib.pyplot as plt
import matplotlib.animation as animation

def InsertionSort(lista):
    fig, ax = plt.subplots()
    ax.bar(range(len(lista)), lista, align='edge')
    for i in range(1, len(lista)):
        for j in range(i, 0, -1):
            if lista[j] < lista[j-1]:
                lista[j], lista[j-1] = lista[j-1], lista[j]
                ax.clear()
                ax.bar(range(len(lista)), lista, align='edge')
                plt.pause(0.1)
            else:
                break
    plt.show()

def BubbleSort(lista):
    for i in range(len(lista),0,-1):
        for j in range(0,(i-1)):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


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

def QuickSort(lista):
    if(len(lista)<=1):
        return lista
    else:
        pivote = lista.pop(0)
        izq = []
        der = []
        for i in lista:
            if i < pivote:
                izq.append(i)
            else:
                der.append(i)
        
        izq = QuickSort(izq)
        der = QuickSort(der)
    return izq + [pivote] + der
