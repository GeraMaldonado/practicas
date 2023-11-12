#Practica algoritmo recursivo

def factorial(x):
    if(x == 1):
        return x
    else:
        print(f"{x}*{x-1}")
        return x * (factorial(x-1))
        


print(factorial(5))
