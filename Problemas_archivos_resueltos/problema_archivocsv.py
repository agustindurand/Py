import pandas as pd

df = pd.read_csv("c:\\Users\\user\\Documents\\Docs\\empresas.csv")
print(df)

df["Presupuesto"] = df["Presupuesto"].astype(str) #Convierte la columna "Presupuesto" del DataFrame df al tipo de dato str (cadena de caracteres).
print (type(df["Presupuesto"][0])) #Nos ejemplifica imprimiendo que clase de dato es 

df["Locacion"].replace("Ciudad X", "Ottawa", inplace=True) #Reemplaza valores en la columna 
print (df)


df = df.drop_duplicates() #Elimina filas repetidas
print (df)

#Creando un nuevo csv con el dataframe resultante

df.to_csv("c:\\Users\\user\\Documents\\Docs\\empresas_archivo_limpios.csv")