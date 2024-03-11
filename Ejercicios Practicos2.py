
#Suponiendo que una persona promedio habla dos palabra por segundo 

#A) Pedirle al usuario que diga cualquier texto real y calcular cuanto tardaria en decir esa frase y cuantas palabras dijo 

ingreso_palabra = input("Ingrese palabra:  ")
palabras = ingreso_palabra.split(" ") #Metodo a fin de contar las palabras con el espacio
cantidad_de_palabras = len(palabras)
print (f"Dijiste {cantidad_de_palabras} palabras y tardarias {cantidad_de_palabras/2} segundos en decirlo")
if cantidad_de_palabras > 240:
     print ("Stop")


