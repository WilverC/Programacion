import pandas as pd
import numpy as np

dataframe = pd.DataFrame({'c1': list('123') , 'clave':list('abc')})
dataframe2 = pd.DataFrame({'c2': list('456') , 'clave':list('cbe')})

print( dataframe )
print( dataframe2 )

#busca por clave los parecidos
dataframe3 = pd.DataFrame.merge(dataframe, dataframe2)
print( dataframe3 )

#busca por el tipo en on, ejemplo por clave
dataframe3 = pd.DataFrame.merge(dataframe, dataframe2, on='clave')
print( dataframe3 )

#mantiene las columnas del dataframe
dataframe3 = pd.DataFrame.merge(dataframe, dataframe2, on='clave', how='left')
print( dataframe3 )

#mantiene las columnas del dataframe2
dataframe3 = pd.DataFrame.merge(dataframe, dataframe2, on='clave', how='right')
print( dataframe3 )

#pone todas ls filas de todo el dataframe, union completa
dataframe3 = pd.DataFrame.merge(dataframe, dataframe2, on='clave', how='outer')
print( dataframe3 )


print("_"*30)
#concatenacion
array = np.arange(9).reshape(3,3)
print(array)

print( np.concatenate([array, array]) )
print( np.concatenate([array, array], axis=1) )

serie1 = pd.Series( list('123'), index=list('abc'))
serie2 = pd.Series( list('456'), index=list('def'))

print( serie1 )
print( serie2 )

print( pd.concat([serie1, serie2]) )

print( pd.concat([serie1, serie2], keys = ['serie1', 'serie2'] ) )

dataframe = pd.DataFrame( np.random.rand(3,3), columns= list('abc') )
dataframe2 = pd.DataFrame( np.random.rand(2,3), columns= list('abc') )
dataframe3 = pd.concat( [ dataframe, dataframe2 ] )
print( dataframe )
print( dataframe2 )
print( dataframe3 )
print( pd.concat( [ dataframe, dataframe2 ], ignore_index=True ) )

print("_"*30)
###combinar series y dataframes
serie1 = pd.Series( [1,2,np.nan] )
serie2 = pd.Series( list('456') )
print( serie1 )
print( serie2 )

serie3 = serie1.combine_first(serie2)
print( serie3 )

lista_valores = [1,2,np.nan]
dataframe = pd.DataFrame( lista_valores )
lista_valores2 = [4,5,6]
dataframe2 = pd.DataFrame( lista_valores2 )
print( dataframe2 )

datafraame3 = dataframe.combine_first(dataframe2)
print( datafraame3 )

print("_"*30)
#duplicados de dataframes
lista_valores = [[1,2], [1,2], [5,6], [5,8]]
lista_indices = list('mnop')
lista_columans= ['valor1', 'valor2']

dataframe = pd.DataFrame(lista_valores, index=lista_indices, columns=lista_columans)
print( dataframe )
print( dataframe.drop_duplicates() ) #quitar valores repetidos

print("_"*30)
#Reemplazar datos en series
serie = pd.Series( list('12345'), index=list('abcde'))
print( serie )

print( serie.replace( 1, 6) ) 

print("_"*30)
#renombrar indices
lista_valores = np.arange(9).reshape(3,3)
lista_indices = list('abc')
dataframe = pd.DataFrame( lista_valores, index= lista_indices )
print( dataframe )

nuevos_indices = dataframe.index.map( str.upper )
dataframe.index = nuevos_indices
print( dataframe )

print("_"*30)
#Agrupar datos
precios = [12,55,48,23,5,21,88,34,26]
rango = [10,20,30,40,50,60,70,80,90,100]

precios_con_rangos = pd.cut( precios, rango )
print( precios_con_rangos )
print( pd.value_counts( precios_con_rangos )  ) 

print("_"*30)
#filtrar datos en dataframes
lista_valores = np.random.rand(10, 3)
print( lista_valores )

datafraame = pd.DataFrame( lista_valores )
print( datafraame )

print( datafraame[0] )
print( datafraame[0] > 0.40)

print("_"*30)
#combinacion de elementos

lista_valores = np.arange(25).reshape(5,5)
print( lista_valores )
datafraame = pd.DataFrame( lista_valores )
print( datafraame )

combinacion_alea = np.random.permutation(5)
print( combinacion_alea )
print( datafraame.take( combinacion_alea ) ) 


print("_"*30)
#agrupacion de dataframes

lista_valores = {'clave1':['x','x','y','y','z'], 'clave2':['a','b','a','b','a'], 
                'datos1': np.random.rand(5), 'datos2':np.random.rand(5) }
print( lista_valores )
dataframe = pd.DataFrame( lista_valores )
print( dataframe )
grupo1 = dataframe['datos1'].groupby( dataframe['clave1'] )
print( grupo1 )
print( grupo1.mean() )

print("_"*30)
#Agregacion operaciones que dan un valor como la media
lista_valores = [list('123'), list('456'), list('789'), [np.nan, np.nan, np.nan] ]
print( lista_valores )
lista_columnas = list( 'abc' )
dataframe = pd.DataFrame( lista_valores, columns=lista_columnas )
print( dataframe )

#print( dataframe.agg(['sum', 'min']) )