import matplotlib.pyplot as plt
import matplotlib.animation as animation

def insertionSort(lista):
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
    return lista

def bubbleSort(lista):
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
    return lista


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
    return lista

def quickSort(lista):
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
        
        izq = quickSort(izq)
        der = quickSort(der)
    return izq + [pivote] + der

def countSort(lista):
    resultado = [0] * len(lista)
    indices = {}
    j = 0
    for i in range(max(lista)+1):
        indices[i] = lista.count(i)
    print(indices)

    for i in range(1,max(lista)+1):
        indices[i] = indices[i-1] + indices[i]
    print(indices)

    for i in lista:
        resultado[indices[i]-1] = i
        indices[i] -= 1
    print(indices)
    return resultado


def radixSort(lista):
    max_num = max(lista)
    exp = 1

    while max_num // exp > 0:
        n = len(lista)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = lista[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = lista[i] // exp
            output[count[index % 10] - 1] = lista[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(n):
            lista[i] = output[i]

        print(f"{lista}")
        exp *= 10
    return lista


def bucketSort(lista):
    maxVal, minVal = max(lista), min(lista)
    bucketRange = (maxVal - minVal) / len(lista)
    buckets = [[] for _ in range(len(lista))]

    for i in lista:
        index = int((i - minVal) // bucketRange)
        buckets[index].append(i)

    for i in range(len(lista)):
        buckets[i] = sorted(buckets[i])

    sortedArr = []
    for i in buckets:
        sortedArr += i

    return sortedArr


