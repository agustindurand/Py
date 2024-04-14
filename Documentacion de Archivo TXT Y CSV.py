
#Archivos TXT

archivo = open ("c:\\Users\\user\\Documents\\Docs\\textoplano.txt", encoding="UTF-8") #Ruta
lineas = archivo.readlines()
print (lineas)
archivo.close #Cerrar archivo #Importante 


 #Si solamente quiero leer una linea en especifico
""" 
linea_uno = archivo.readline () #Se lee la primer linea del archivo
print (linea_uno)

linea_dos = archivo.readline (4) #Lee la cantidad de caracteres que indicamos 
print (linea_dos)

"""

with open ("c:\\Users\\user\\Documents\\Docs\\textoplano2.txt", encoding = "UTF8") as ArchivoUNO: 
   contenido = ArchivoUNO.read()
   print(contenido)
 
 

with open ("c:\\Users\\user\\Documents\\Docs\\textoplano3.txt", "w",  encoding = "UTF8") as ArchivoDOS: #Recibe W que otorga permiso de escritura
     ArchivoDOS.writelines(["Primer ejemplo de Sobreescritura", " ", "y", " ", "segundo ejemplo de sobreescritura"])
     
#Archivos CSV "Comma Separated Values" (Valores Separados por Comas). Es un formato de archivo simple utilizado para almacenar datos en forma de tabla, donde cada línea del archivo representa una fila de datos y los valores individuales están separados por comas u otro delimitador.

import csv #Sentencia que importa la biblioteca estandar CSV

with open ("c:\\Users\\user\\Documents\\Docs\\datos.csv") as archivoscsv:
    reader = csv.reader(archivoscsv)
    for row in reader: #Itera sobre cada fila 
         print(row )
         
import pandas as pd  
print (type(pd))

df = pd.read_csv("c:\\Users\\user\\Documents\\Docs\\datos.csv")
print(df["Name"]) #Obtiene datos de la columna indicada)

#Slicing nos permite identificar principio y final que vamos a acceder a los elementos
#Ejemplo
cadena = "0123456789"
print (cadena[:]) #Muestra cadena completa, si no se especifica
print (cadena[2:6]) #Muestra entre esos valores contenidos


#Acceder a primera/s filas 

primeras_filas=df.head(2)
print (primeras_filas)

#Indica cantidad de filas y columnas@

filas_columas_totales = df.shape
print(filas_columas_totales)

#Ordenar dataframe

df_ordenado_por_edad = df.sort_values("Age",ascending=False)
print (df_ordenado_por_edad)


