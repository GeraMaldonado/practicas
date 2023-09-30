lista = [7,3,10,1,9]
print(lista)
for i in range(1,len(lista)):
    for j in range(i,0,-1):
        if lista[j]<lista[j-1]:
            lista[j],lista[j-1] = lista[j-1], lista[j]
        else:
            break
print(lista)

