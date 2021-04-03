
''' ----------- Condicionales ------------
### sentencias de if, switch, etc
### tomar deciciones con  base a el resultado
### dado por la condicion
'''

codigo_postal = [42154, 42367, 43434, 42756]

print("---------- condicion if-----------")
for cp in codigo_postal:
    if(cp == 43434):
        print("codigo postal : ",cp, "es correcto")

print("---------- condicion elif --------------")
for cp in codigo_postal:
    if(cp == 43434):
        print("codigo postal : ",cp, "es correcto")
    elif(cp == 42154):
        print("codigo postal : ",cp, "es correcto")

print("---------- condicion else ----------")
for cp in codigo_postal:
    if(cp == 43434):
        print("codigo postal : ",cp, "es correcto")
    elif(cp == 42154):
        print("codigo postal : ",cp, "es correcto")
    else:
        print("codigo postal : ",cp, "es incorreto")


print("----- Comparaciones----------")
print("---- con == ----------")
carro = 'audi'
print(carro == 'bmw')
print(carro == 'audi')
print("------ con != -----------")
print(carro != 'audi')
print(carro != 'bmw')

