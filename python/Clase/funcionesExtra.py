#funciones generadoras
rango = range(0, 11) 
print( rango )

for i in range(0, 11):
    print( i )

#solo devuelve cada uno con yield
def pares(maximo):
    for i in range(maximo):
        if( i % 2 == 0):
            yield i

for numero in pares(11):
    print(numero)


### Filter - Funcion para filtrar resultados segun su condicion
def positivo(numero):
    if( numero > 0):
        return True
    else:
        return False

numeros = [4, -2, 8, -3, -5, -7, 1, 9]
filtro = filter(positivo, numeros)
resultado = list(filtro)

print(resultado)


###Map - Aplicar una funcion a una lista
def multiplicar(numero):
    return numero * 2

numeros = [2,4,6]
mapeo = map(multiplicar, numeros)
mapeo
resultado = list(mapeo)
print(resultado)