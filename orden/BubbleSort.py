import random
import time
#lista = [7,3,10,1,9]
lista = random.sample(range(1,1001),1000)
#print(lista)
inicio = time.time()
for i in range(len(lista),0,-1):
    for j in range(0,(i-1)):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
fin = time.time()
#print(lista)
print(f"Tiempo con BubbleSort: {fin-inicio}")
