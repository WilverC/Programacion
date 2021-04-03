
'''
### ---------- Diccionarios -------------
### los diccionarios son una coleccion de 
### pares llave-valor guardado entre {}
### cada llave esta conectada a un valor y
### pueden ser de tipo: numeros, cadenas, listas, etc.
###
'''

'''---------- Inicializacion --------------- '''
#diccionario vacio
dic = {}
print(type(dic))
print(dic)

#diccionario inicializado
dic = {'canal': 'youtube',
        'redsocial': 'facebook',}
print(dic)

'''-------- Acceder con la llave --------------------'''
print(dic['canal'])

'''-------- Añadir valores ------------------- '''
print("Agregar----------------------------------------")
dic['descripcion'] = "Videos para aprender"
dic['categoria'] = "formacion"
print(dic)

'''---------Modificar----------------'''
print("Modificar----------------------------------------")
dic['categoria'] = "Entretenimiento"
print(dic)

'''---------Eliminar elementos-----------------'''
print("Eliminar----------------------------------------")
del dic['descripcion']
print(dic)

dic = {
    '1984': 'George Orwell',
    'Rebelion en la granja' : 'George Orwell',
    'Caballos Desbocados': 'Yukio Mishima',
    'Caballos Desbocados': 'Yukio 2',
}

''' -------recorrer con for ------------------ '''
print("items-------------------")
#por los items
for key, value in dic.items():
    print("key: " + key)
    print("value: " + value)

print("llaves-------------------")
#por los keys
for value in dic.keys():
    print("value: "+ value)

print("valores-------------------")
#por los value
for key in dic.values():
    print("value: "+ key)

#evitar duplicidad
print("duplicidad-------------------")
for libro in set(dic.keys()):
    print("value: "+ libro)







