import matplotlib.pyplot as plt
import matplotlib.animation as animation

def InsertionSort(lista):
    fig, ax = plt.subplots()
    barras = ax.bar(range(len(lista)), lista, align='edge')

    for i in range(1, len(lista)):
        for j in range(i, 0, -1):
            if lista[j] < lista[j-1]:
                lista[j], lista[j-1] = lista[j-1], lista[j]

                ax.clear()
                barras = ax.bar(range(len(lista)), lista, align='edge', color='blue')

                barras[j].set_color('red')
                barras[j-1].set_color('red')

                plt.pause(.1)
            else:
                break
    barras = ax.bar(range(len(lista)), lista, align='edge')
    plt.show()

def BubbleSort(lista):
    fig, ax = plt.subplots()
    barras = ax.bar(range(len(lista)), lista, align='edge')

    for i in range(len(lista),0,-1):
        for j in range(0,(i-1)):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

                ax.clear()
                barras = ax.bar(range(len(lista)), lista, align='edge', color='blue')

                barras[j].set_color('red')
                barras[j+1].set_color('red')
                plt.pause(.1)
    barras = ax.bar(range(len(lista)), lista, align='edge')
    plt.show()


def mergeSort(lista):
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(lista)), lista, align='edge', color='blue')
    plt.pause(0.1)

    def separar(x, start, end):
        nonlocal bars
        if end - start <= 1:
            return [x[start]]

        mediana = start + (end - start) // 2
        izquierda = separar(x, start, mediana)
        derecha = separar(x, mediana, end)
        ultimo_izquierda = len(izquierda)

        if izquierda[ultimo_izquierda - 1] <= derecha[0]:
            izquierda.extend(derecha)
            for i in range(len(izquierda)):
                bars[start + i].set_height(izquierda[i])
                bars[start + i].set_color('green')  # Cambiar color de las barras unidas
            plt.pause(0.1)
            return izquierda

        resultado = orden(izquierda, derecha, start, mediana, end)
        for i in range(len(resultado)):
            bars[start + i].set_height(resultado[i])
            bars[start + i].set_color('orange')  # Cambiar color de las barras ordenadas
        plt.pause(0.1)
        return resultado

    def orden(x, y, start, mediana, end):
        resultado = []
        while len(x) > 0 and len(y) > 0:
            if x[0] <= y[0]:
                resultado.append(x[0])
                del x[0]
            else:
                resultado.append(y[0])
                del y[0]

        if len(x) > 0:
            resultado.extend(x)

        if len(y) > 0:
            resultado.extend(y)

        for i in range(len(resultado)):
            bars[start + i].set_height(resultado[i])
            bars[start + i].set_color('purple')  # Cambiar color de las barras combinadas
        plt.pause(0.1)
        return resultado

    separar(lista, 0, len(lista))
    plt.show()
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
