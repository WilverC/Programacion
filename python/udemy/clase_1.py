#Variables

cadena = "Hola mundo"
numero = 6


print(cadena,numero)

print (type(cadena))
print (type(numero))

cadena2 = str(numero)
print(cadena2)
print(type(cadena2))


numero2 = int("50")
print(numero2)
print(type(numero2))

#posiciones de la cadena
#"H o l a   m u n d o"
# 1 2 3 4 5 6 7 8 9 10

print(cadena[0])
print(cadena[1])
print(cadena[2])
print(cadena[3])
print(cadena[4])

print(cadena[-1])
print(cadena[1:5])
print(cadena[3:7])

#funciones de cadena
tam = len(cadena)
print(tam)

mayus = cadena.upper()
print(mayus)


minus = mayus.lower()
print(minus)

cadena3 = "lista1,lista2,lista3,lista4"
lista = cadena3.split(',')
print(lista)
print(type(lista))

##impresion
cadena4 = "mundo"
print("Hola "+ cadena4)


#formato
cadena = "Alejandra"
amor = 100
print("Jovanny ama a {} el {}%".format(cadena,amor))
print("Jovanny ama a {nom} el {num}%".format(nom=cadena,num=amor))
print("Jovanny ama a {} el {num:1.3f}%".format(cadena,num=amor))

#f-string
print(f"Buenos dias {cadena}, hoy cumples {amor} años")


#entrada por teclado
print("Introduzca un nombre")
nombre = input()
print(f"Hola {nombre}")