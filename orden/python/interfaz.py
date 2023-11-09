import tkinter


#Declarar funiones para los botones
def hola():
    print("Hola")


#Iniciar nuestra ventana
ventana = tkinter.Tk()


#Direccionar la venta
ventana.geometry("400x300")

#Crear etiqueta
etiqueta = tkinter.Label(ventana, text = "Hola mundo", bg = "blue")
#Para que aparezca en la ventana
#dentro de pack fill se usa para estirar, y side para posicionar
etiqueta.pack()


#Creacion de botones
boton1 = tkinter.Button(ventana, text = "Presiona", padx = 40, pady = 50, command = hola)
boton1.pack()



#Ingresar una caja de texto
#Se puede escpecificar una fuente (font=) y un tamaño
cajaTexto = tkinter.Entry(ventana)
cajaTexto.pack()


def textodeCaja():
    entrada = cajaTexto.get()
    print(entrada)

#Para recuperar el texto
boton2 = tkinter.Button(ventana, text = "enviar", command = textodeCaja)
boton2.pack()


#Posicionamiento metodo GRID

#boton3 = tkinter.Button(ventana, text = "boton3", width = 10, height = 5)
#boton4 = tkinter.Button(ventana, text = "boton4", width = 10, height = 5)
#boton5 = tkinter.Button(ventana, text = "boton5", width = 10, height = 5)

#boton3.grid(row = 3, column = 0)
#boton4.grid(row = 3, column = 1)
#boton5.grid(row = 3, column = 2)


#Registro de actividades
ventana.mainloop()






