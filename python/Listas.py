'''
*
*Autor: Jovanny Wilver Cortez Enriquez
*Descripción: Operaciones básicas con listas simples 
'''

'''Trabajando con listas'''

'''-------Creación de lista-------'''
print("Creacion----------------------------------------")
#lista vacia
lista = []
print(type(lista))
print(lista)

#lista inicializada
lista2 = ["Esto","tiene", 4,"elementos"]
print(type(lista2))
print(lista2)

#acceder por indice al elemento
elemento = lista2[3]
print(elemento)

'''-------Agregar elementos a una lista----'''
print("Agregar----------------------------------------")
#al final de la lista
lista2.append("saludos")
print(lista2)

#por indice
lista2.insert(1,"no")
print(lista2)

'''---------Modificar----------------'''
print("Modificar----------------------------------------")
#por indice
lista2[5] = "terminado"
print(lista2)

'''---------Eliminar elementos-----------------'''
print("Eliminar----------------------------------------")
#por indice
del lista2[0]
print(lista2)

#puede ser ocupado por otro
elemento = lista2.pop()
print(elemento)
print(lista2)

#por indice pero puede ser ocupado
elemento = lista2.pop(1)
print(elemento)
print(lista2)

#por valor de la lista
lista2.remove("no")
print(lista2)

'''--------------Ordenar una lista----------------'''
print("Orden----------------------------------------")
#ascendente
lista = ["C","a","U","x","d","m","A"]
print(lista)
lista.sort()
print(lista)

#descendente
lista.reverse()
print(lista)

#ascendente
sorted(lista)
print(lista)

''' ---------------funciones------------------ '''
print("Funciones----------------------------------------")
lista = [1,2,3,4,5,6,7]
#el valor minimo de una lista
mini = min(lista)
print(mini)
#el valor maximo de una lista
maxi = max(lista)
print(maxi)
#suma de todos los valores de la lista
suma = sum(lista)
print(suma)

'''----------------otros-----------------------'''
print("Otros----------------------------------------")
#longitud de una lista
tam = len(lista)
print(tam)

#crear lista a partir de list y range
lista = list(range(1,6))
print(lista)

#range saltos de n numeros n=2
lista = list(range(1,20, 2))
print(lista)


''' --------------Comprension -------------------- '''
print("por comprension------------------------")
cuadrado = [valor**2 for valor in range(1,11)]
print(cuadrado)


''' --------------Rebanada------------------------- '''
print("Rebanada-----------------------------------")
alumnos = ['Carlitos', 'Juanito', 'Manganito', 'Peranganito']
print(alumnos[0:3])
print(alumnos[:2])
print(alumnos[2:])

print("con ciclo---------------------------------------")
for alumno in alumnos[:3]:
    print(alumno)


print("copias------------------------------------------")
mis_comidas = ['Platano', 'Banana', 'Tortas', 'taquitos', 'Tamales']
comidas_amigos = mis_comidas[:]
print(comidas_amigos)

mis_comidas.append('Huevos al gusto')
comidas_amigos.append('Sandwich')
print(comidas_amigos)






