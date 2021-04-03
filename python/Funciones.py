
'''
### -----------Funciones ---------------
### las funciones agilizan los códigos
### evitan el código repetititvo
### 
'''

# Funcion basica'
def saludo():
    print("Hola camarada")

saludo()


#Con parametros
def potencia(n):
    print(n**2)

potencia(5)


#retorno de datos
def potencia(n, p):
    return n**p

pot = potencia(2,4)
print("El valor de: ",pot)