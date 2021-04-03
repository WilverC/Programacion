import tkinter
import pygame

ventana = tkinter.Tk()
ventana.geometry("400x300")

#etiquetas, se usa pack apra posicion sea con fill o side
#etiqueta = tkinter.Label(ventana,text="Hola Mundo", bg ="blue")
#etiqueta.pack(side= tkinter.BOTTOM)

def saludo():
	print("Hola")

#botones
#usar lambda
#boton1 = tkinter.Button(ventana, text="Presiona", command = saludo)
#boton1.pack()

#Cajas de texto
cajaTexto = tkinter.Entry(ventana, font="Helvetica 50")
cajaTexto.pack()

def textoDeLaCaja():
	text20 = cajaTexto.get()
	print(text20)

boton2 = tkinter.Button(ventana, text="Presiona", command = textoDeLaCaja)
boton2.pack()

ventana.mainloop()