lista = [8,3,1,19,14]
print(lista)
for i in range(len(lista),0,-1):
    for j in range(0,(i-1)):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
print(lista)
