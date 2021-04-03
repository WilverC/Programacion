from tkinter import *
from typing import Pattern

ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("430x600")
ventana.resizable(False, False)
ventana.configure( background="gray")

#funciones
operacion = ""
resultado = StringVar()

def borrar():
    global operacion
    global resultado
    operacion = ""
    pantalla.delete(0,END)

def pulsar( valor ):
    global operacion
    global resultado
    operacion = operacion + str(valor)
    pantalla.delete(0,END)
    pantalla.insert(0, operacion)

def calcular():
    global operacion
    global resultado
    try:
        resultado = str( eval(operacion) )
    except:
        resultado = "Error"
    finally:
        pantalla.delete(0,END)
        pantalla.insert(0, resultado)


#Display de resultados
pantalla = Entry( ventana, font=("arial", 20, "bold"), borderwidth=2)
pantalla.grid(row=0, column=0, columnspan=3, pady=10, padx=5)

#boton de reiniciar
boton_reset = Button( ventana, text="AC", width=8, height=2, command=lambda:borrar() )
boton_reset.grid( row=0, column=3, pady=10)

#botones de la primera fila
ancho = 8
alto = 3
bordex = 5
bordey = 5

boton_1 = Button(ventana, text="1", width=ancho, height=alto, command=lambda:pulsar("1") )
boton_1.grid(row=1, column=0, padx = bordex, pady = bordey )
boton_2 = Button(ventana, text="2", width=ancho, height=alto, command=lambda:pulsar("2") )
boton_2.grid(row=1, column=1, padx = bordex, pady = bordey )
boton_3 = Button(ventana, text="3", width=ancho, height=alto, command=lambda:pulsar("3") )
boton_3.grid(row=1, column=2, padx = bordex, pady = bordey )
boton_4 = Button(ventana, text="4", width=ancho, height=alto, command=lambda:pulsar("4") )
boton_4.grid(row=1, column=3, padx = bordex, pady = bordey )

#botones de la segunda fila
boton_5 = Button(ventana, text="5", width=ancho, height=alto, command=lambda:pulsar("5") )
boton_5.grid(row=2, column=0, padx = bordex, pady = bordey )
boton_6 = Button(ventana, text="6", width=ancho, height=alto, command=lambda:pulsar("6") )
boton_6.grid(row=2, column=1, padx = bordex, pady = bordey )
boton_7 = Button(ventana, text="6", width=ancho, height=alto, command=lambda:pulsar("7") )
boton_7.grid(row=2, column=2, padx = bordex, pady = bordey )
boton_8 = Button(ventana, text="8", width=ancho, height=alto, command=lambda:pulsar("8") )
boton_8.grid(row=2, column=3, padx = bordex, pady = bordey )

#botones de la tercera fila
boton_9 = Button(ventana, text="9", width=ancho, height=alto, command=lambda:pulsar("9") )
boton_9.grid(row=3, column=0, padx = bordex, pady = bordey )
boton_0 = Button(ventana, text="0", width=ancho, height=alto, command=lambda:pulsar("0") )
boton_0.grid(row=3, column=1, padx = bordex, pady = bordey )
boton_punto = Button(ventana, text=".", width=ancho, height=alto, command=lambda:pulsar(".") )
boton_punto.grid(row=3, column=2, padx = bordex, pady = bordey )
boton_suma = Button(ventana, text="+", width=ancho, height=alto, command=lambda:pulsar("+") )
boton_suma.grid(row=3, column=3, padx = bordex, pady = bordey )

#botones de la cuarta fila
boton_resta = Button(ventana, text="-", width=ancho, height=alto, command=lambda:pulsar("-") )
boton_resta.grid(row=4, column=0, padx = bordex, pady = bordey )
boton_multi = Button(ventana, text="*", width=ancho, height=alto, command=lambda:pulsar("*") )
boton_multi.grid(row=4, column=1, padx = bordex, pady = bordey )
boton_divi = Button(ventana, text="/", width=ancho, height=alto, command=lambda:pulsar("/") )
boton_divi.grid(row=4, column=2, padx = bordex, pady = bordey )
boton_resul = Button(ventana, text="=", width=ancho, height=alto, command=lambda:calcular() )
boton_resul.grid(row=4, column=3, padx = bordex, pady = bordey )


ventana.mainloop()