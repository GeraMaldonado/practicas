import tkinter
import orden

x =[7,4,8,3,1]
print(x)


def insertion():
    print(x)
    print(orden.InsertionSort(x))
def bubble():
    print(x)
    print(orden.BubbleSort(x))
def merge():
    print(x)
    print(orden.mergeSort(x))
def quick():
    print(x)
    print(orden.QuickSort(x))





ventana = tkinter.Tk()
ventana.geometry("400x300")
etiqueta = tkinter.Label(ventana, text = "Ordenamiento")
etiqueta.pack()


insertion = tkinter.Button(ventana, text = "Insertion Sort", command = insertion)
insertion.pack()
bubble = tkinter.Button(ventana, text = "Bubble Sort", command = bubble)
bubble.pack()
merge = tkinter.Button(ventana, text = "Merge Sort", command = merge)
merge.pack()
quick = tkinter.Button(ventana, text = "QuickSort", command = quick)
quick.pack()
ventana.mainloop()

