### HTML y EXCEL

import pandas as pd

url = 'https://es.wikipedia.org/wiki/Anexo:Finales_de_la_Copa_Mundial_de_F%C3%BAtbol'

dataframe = pd.io.html.read_html(url)
print( dataframe )

#fichero_excel = pd.ExcelFile('archivo.xlsx') #Direccion de el archivo
#dataframe = fichero_excel.parse('Hoja 1')
#dataframe2 = pd.read_csv('archivo.csv')