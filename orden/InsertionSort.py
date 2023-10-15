import random
import time
#lista = [7,3,10,1,9]
lista = random.sample(range(1,1001),1000)
#print(lista)
inicio = time.time()
for i in range(1,len(lista)):
    for j in range(i,0,-1):
        if lista[j]<lista[j-1]:
            lista[j],lista[j-1] = lista[j-1], lista[j]
        else:
            break
fin = time.time()
#print(lista)
print(f"Tiempo con InsertionSort: {fin-inicio}")

