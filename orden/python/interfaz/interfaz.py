import tkinter
import orden

def insertion():
    resultado = orden.insertionSort(lista)
    actualizar_resultado(resultado)

def bubble():
    resultado = orden.bubbleSort(lista)
    actualizar_resultado(resultado)

def merge():
    resultado = orden.mergeSort(lista)
    actualizar_resultado(resultado)

def quick():
    resultado = orden.quickSort(lista)
    actualizar_resultado(resultado)

def counting():
    resultado = orden.countSort(lista)
    actualizar_resultado(resultado)

def radix():
    resultado = orden.radixSort(lista)
    actualizar_resultado(resultado)

def bucket():
    resultado = orden.bucketSort(lista)
    actualizar_resultado(resultado)

def actualizarLista():
    global lista
    nuevaLista = entrada.get()
    lista = obtenerLista(nuevaLista)
    etiquetaResultado.config(text=f"Lista actualizada: {lista}")
    actualizar_resultado("")

def obtenerLista(x="7,4,8,3,1,5,4,8,6,3,2,5,4,8,7,3,5,2,1"):
    return list(map(int, x.split(",")))

def actualizar_resultado(resultado):
    widget_resultado.config(state=tkinter.NORMAL)
    widget_resultado.delete("1.0", tkinter.END)  # Limpiar contenido actual
    widget_resultado.insert(tkinter.END, resultado)
    widget_resultado.config(state=tkinter.DISABLED)

lista = obtenerLista()

ventana = tkinter.Tk()
ventana.geometry("600x500")
etiqueta = tkinter.Label(ventana, text="Ordenamiento")
etiqueta.pack()

insertion = tkinter.Button(ventana, text="InsertionSort", command=insertion)
insertion.pack()
bubble = tkinter.Button(ventana, text="BubbleSort", command=bubble)
bubble.pack()
merge = tkinter.Button(ventana, text="MergeSort", command=merge)
merge.pack()
quick = tkinter.Button(ventana, text="QuickSort", command=quick)
quick.pack()
counting = tkinter.Button(ventana, text="CountingSort", command=counting)
counting.pack()
radix = tkinter.Button(ventana, text="RadixSort", command=radix)
radix.pack()
bucket = tkinter.Button(ventana, text="BucketSort", command=bucket)
bucket.pack()

entrada = tkinter.Entry(ventana, width=30)
entrada.pack(pady=10)

boton = tkinter.Button(ventana, text="Ingresa tu lista", command=actualizarLista)
boton.pack(pady=10)

etiquetaResultado = tkinter.Label(ventana, text=f"Lista actual: {lista}")
etiquetaResultado.pack(pady=10)

# Crear un widget Text para mostrar el resultado del ordenamiento
widget_resultado = tkinter.Text(ventana, wrap="word", height=10, width=60)
widget_resultado.pack(pady=10)
widget_resultado.config(state=tkinter.DISABLED)

ventana.mainloop()
