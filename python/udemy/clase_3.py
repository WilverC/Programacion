
#listas
print("listas, son modificables")
colores = ["rojo","amarillo","verde"]
print(colores[0])
print(f"tamaño {len(colores)}")
print("agregamos un color")
colores.append("azul")
print(colores)
print("Borramos rojo")
colores.remove("rojo")
print(colores)
print("ordenar alfabeticamente")
colores.sort()
print(colores)
print("borrar todo")
colores.clear()
print(colores)

#tuplas
print("\n\n")
print("tuplas, no son modificables, solo de lectura")
colort = ("rojo","amarillo","verde")
print(colort[1])
print(f"tamaño {len(colort)}")

#conjuntos
print("\n\n")
print("conjutnos, coleccion de elementos desordenado")
coloresc = {"rojo","amarillo","verde"}
print(coloresc)
print(f"tamaño {len(coloresc)}")
print("agregamos un elemento")
coloresc.add("azul")
print(coloresc)
print("borramos rojo")
coloresc.remove("rojo")
print(coloresc)

#diccionarios
print("\n\n")
print("Diccionarios, coloccion de elementos no indexados, formado por clave-valor")

diccolores = {"red":"rojo","yellow":"amarillo","green":"verde"}

print(diccolores)
print("acceder al valor por clave")
print(diccolores["red"])
print("agregamos elemento")
diccolores["black"] = "negro"
print(diccolores)
print("Borramos por un pop")
diccolores.pop("yellow")
print(diccolores)
del(diccolores["red"])
print(diccolores)

