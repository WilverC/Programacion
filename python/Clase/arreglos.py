##arreglos

import numpy as np

print( np.zeros(4) ) 
print( np.ones(4) )
print( np.arange(5) ) 
print( np.arange(2,20,3) ) 


print("*"*20)
array1 = np.array([1,2,3,4,5,6])

print( array1+2)
print( array1-2)
print( array1*2)
print( array1/2)
print(array1.dtype)

print("*"*20)
###indexacion
array = np.arange(0,11)
print(array[0:3])
print(array[:])

array_copia = array.copy()
print(f"copia {array_copia}")
array_copia = array_copia + 10
print(f"copia {array_copia}")



print("*"*20)
###matrices transpuestas

array = np.arange(15).reshape((3,5))
print(array)
array_Trans = array.T
print(array_Trans)


print("*"*20)
###entrada y salida de arrays
array2 = np.arange(6)
print(array2)

np.save('array1s',array2)
np.load('array1s.npy')

array = np.arange(6)
array = array + 10
np.savez('arrays',x = array, y = array2)
array_recuperado = np.load('arrays.npz')
print( array_recuperado['x'] )
print( array_recuperado['y'] )

array2 = array2 * 2
np.savetxt('mificheroarray.txt',array2,delimiter=',')
salvadotxt = np.loadtxt('mificheroarray.txt',delimiter=',')
print( salvadotxt )

print("*"*20)
###funciones con array
array = np.arange(5)
array2 = np.arange(5) * 3

print( np.sqrt(array) )
print( np.random.rand(5) )
print( np.random.rand(5) )
suma = np.add(array, array2)
print(suma)
