###Modulo pandas

###Series

from numpy.core.fromnumeric import reshape
import pandas as pd

series1 = pd.Series([3,5,7])
print(series1)

asignaturas = ['matematicas', 'historia', 'fisica', 'literatura']
notas_ale = [8, 6, 9, 7]
serie_notas_ale = pd.Series(notas_ale, index=asignaturas)
serie_notas_ale.name = 'Notas Ale'
serie_notas_ale.index.name = 'Asignaturas'
print(serie_notas_ale)

#Convertir a diccionario
diccionario = serie_notas_ale.to_dict()
print( diccionario )

#viceversa
serie = pd.Series(diccionario)
print( serie )

asignaturas = ['matematicas', 'historia', 'fisica', 'literatura']
notas_jova = [8, 6, 9, 7]
serie_notas_jova = pd.Series(notas_jova, index=asignaturas)

notas_clase = (serie_notas_ale + serie_notas_jova) / 2
print(notas_clase)


###DataFrame

import webbrowser
#website = 'https://es.wikipedia.org/wiki/Anexo:Campeones_de_la_NBA'
#webbrowser.open(website)
"""
#obtiene lo que esta en buffer o lo que se haya copiado
dataframe_nba = pd.read_clipboard()
print( dataframe_nba )

print( dataframe_nba.columns )  #muestra las columnas existentes
print( dataframe_nba.loc[5] )   #recuperar por indice
print( dataframe_nba.head ) #muestra los primeros 5 elementos
print( dataframe_nba.tail)  #muestra los 5 ultimos elementoss
"""

print("_"*20)
### Indices
lista_valores = [1,2,3]
lista_indices = ['a','b','c']
serie = pd.Series( lista_valores, index=lista_indices)
print( serie )
print( serie.index )    #con index[valor] imprime su valor del indice

lista_valores = [[6,7,8],[8,9,5],[6,9,7]]
lista_indices = ['matematicas', 'historia', 'fisica']
lista_nombres = ['Alejandra', 'Lizeth', 'Jovanny']

dataframe = pd.DataFrame(lista_valores, index=lista_indices, columns=lista_nombres)
print( dataframe )

print("_"*20)
###eliminar elementos
import numpy as np

serie = pd.Series( np.arange(4), index=['a','b','c','d'])
print( serie )
print( serie.drop('c') )

lista_valores = np.arange(9).reshape(3,3)
lista_indices = ['a','b','c']
lista_columnas = ['c1','c2','c3']
dataframe = pd.DataFrame( lista_valores, index=lista_indices, columns=lista_columnas)
print( dataframe )
print( dataframe.drop('b') )
print( dataframe.drop('c2',axis=1) )

print("_"*20)
###seleccion de datos en series
lista_valores = np.arange(3)
lista_indices = ['i1','i2','i3']
serie = pd.Series( lista_valores, index=lista_indices)
serie = serie * 2
print( serie )
print( serie['i2'] )
print( serie[2] )
print( serie[0:2] )

print("_"*20)
###seleccion de datos de un dataframe
lista_valores = np.arange(25).reshape(5,5)
lista_indices = ['i1','i2','i3','i4','i5']
lista_columnas = ['c1','c2','c3','c4','c5']

dataframe = pd.DataFrame( lista_valores, index=lista_indices, columns=lista_columnas)
print( dataframe )
print( dataframe['c2'] )    #posicion de columnas
print( dataframe['c2']['i2'] )
print( dataframe[['c3','c4']] )
print( dataframe.loc['i3'] )        #posicion de filas
print( dataframe.loc['i3']['c4'] )

print("_"*20)
###operaciones de series y dataframes

serie1 = pd.Series([0,1,2], index=['a','b','c'])
serie2 = pd.Series([3,4,5,6], index=['a','b','c', 'd'])

print( serie1 )
print( serie2 )
print( serie1 + serie2 )

lista_valores = np.arange(4).reshape(2,2)
lista_indices = list('ab')
lista_columnas = list('12')
dataframe = pd.DataFrame(lista_valores, index=lista_indices,columns=lista_columnas)
print( dataframe )

lista_valores2 = np.arange(9).reshape(3,3)
lista_indices2 = list('abc')
lista_columnas2 = list('123')
dataframe2 = pd.DataFrame(lista_valores2, index=lista_indices2,columns=lista_columnas2)
print( dataframe2 )

print( dataframe + dataframe2 )
print( dataframe.add( dataframe2, fill_value=0) ) 


print( "_"*20)
###ordenar y clasificar
lista_valores = range(4)
lista_indices = list('CABD')
serie = pd.Series( lista_valores, index=lista_indices)
print( serie )
print( serie.sort_index() )
print( serie.sort_values() )
print( serie.rank() )

serie2 = pd.Series(np.random.rand(10))
print( serie2 )
print( serie2.rank() )
print( serie2.sort_values() )

print("_"*20)
###estadisticas en dataframes

array = np.array([[1,8,3],[5,6,7]])
print( array )
dataframe = pd.DataFrame( array, index=['a', 'b'], columns=list('123'))
print(dataframe)
print( dataframe.sum() )
print( dataframe.sum(axis=1) )
print( dataframe.min() )
print( dataframe.max() )
print( dataframe.min(axis=1) )
print( dataframe.max(axis=1) )
print( dataframe.idxmin() )
print( dataframe.describe() )   #estadistica

print("_"*20)
###valores nulos
lista_valores = ['1','2',np.nan,'4']
serie = pd.Series(lista_valores, index=list('abcd'))

print( serie )
print( serie.isnull() )
print( serie.dropna() )

lista_valores = [[1,2,3], [4,np.nan, 5], [6,7,np.nan]]
lista_indices = list('123')
lista_columnas = list('abc')
dataframe = pd.DataFrame( lista_valores, index=lista_indices, columns=lista_columnas)

print( dataframe )
print( dataframe.isnull() )
print( dataframe.dropna() )
print( dataframe.fillna(0) )

print("_"*20)
###jerarquia de indices
lista_valores = np.random.random(6)
lista_indices = [[1,1,1,2,2,2],['a','b','c','a','b','c']]

series = pd.Series( lista_valores, index=lista_indices)
print( series )
print( series[1] )
print( series[1]['b'] )

dataframe = series.unstack()
print( dataframe )

lista_valores = np.arange(16).reshape(4,4)
lista_indices = list('1234')
lista_columnas = list('abcd')
dataframe = pd.DataFrame( lista_valores, index=lista_indices, columns=lista_columnas)
print( dataframe )
serie2 = dataframe.stack()
print( serie2 )



