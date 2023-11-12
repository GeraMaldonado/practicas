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

lista = [5,2,7,3,1,8,2,6,9]
print(QuickSort(lista))
