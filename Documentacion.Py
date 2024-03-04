

#Documentacion de Curso de Python 

#1. Impresion 
print("hello world")
print ("hola mundo")

#2. 

# Tipo de dato String (Texto en una sola linea)
"String"

""""string""" 

#Tipo de dato Int
400
2
23456
122

#Tipo de Dato Float
4,5
222,1
50000,0

#Tipo de dato Boolean
True
False 

#3. Variables
#Declaracion, Asignacion 

a = 1222
b = 123333
c = 13,5
d= "ABC"
suma = 50 + 100

#Redefinicion de Variable

d = "DDDXXX"

print(c)

nombre = " Tu nombre "
print("Ingresa" +  nombre)

numero = 12
numero += 29 

#Concatenacion 

nombre_primero = "Trevor"
bienvenido = "Hello  " + nombre_primero + " Como estas?"
print (bienvenido)

#Concatenar con f-strings
bienvenido = f"Hello {nombre_primero} Como estas?"

#Operador de pertenencia (IN / NOT IN)
bienvenida = "Lucia"
print ("uci" in bienvenida)

#4.Datos compuestos 

#(Listas)
lista = ["Luke", "Yes", False, 1,222, 2001]
print(lista)
print(lista[2])

#(Tuplas)
tupla = ("Luke", "Yes", False, 1,222, 2001) #No se puede modificar, la lista si

#Dict

diccionario = {
    "name" : "Trevor",
    "lastname" : "Rogers",
    "height" : 1.81
}

print(diccionario["lastname"])


#5.Operadores Aritmeticos 

#Suma y Resta (+ / -)
#Multiplicacion y Division (* /  / )

#Potenciacion (**)

exponente = 12**2

#Division baja (//)
division_baja = 12//2 #Devuelve entero redondeado

#Resto o modulo
resto = 12 % 5  #Devuelve entero redondeado

print (exponente)
print (division_baja)
print(resto)

#Typle
tipo_dato = type(resto)
print (tipo_dato)


#6.Operadores de Comparacion

Igual = 5 == 6 #Devuelven True o False 
Distinto = 5 != 2
mayor = 5 > 2 
menor = 5 < 2
mayor_igual = 4 >= 2
menor_igual = 4 <= 2


contrasena_almacenada = "XXXXXXX"
contrasena_escrita = "YYYYYY"

print (contrasena_almacenada == contrasena_escrita)

#7. Condicionales

edad = 17 

if edad >= 18:
    print ("Podes pasar")
else:
    print ("No podes")
    
    
# Else- If (Elif)

Ingreso = 100000

if Ingreso > 100000:
    print ("Estable")
elif Ingreso > 10000:
    print ("Acertado")
else:
    print("Inestable")
    
#8. Operadores Logicos

#AND
Resultado = True & True #Devuelve True
Resultado2 = False & True #Devuelve Falso
Resultado3 = True & False #Devuelve Falso
Resultado4 = False & True #Devuelve Falso

#OR
Resultado5= True | True #Devuelve True
Resultado6= False | True #Devuelve True
Resultado7= True | False #Devuelve True
Resultado8= False | False #Devuelve False

#NOT
Resultado9= not True #Devuelve Falso
Resultado10= not False #Devuelve True

#Metodos de CADENAS


cadena1 = "Welcome"
cadena2 = "Trevor"

print(dir(cadena1)) #Dir indica la cantidad de funciones que podemos emplear

mayusc = cadena2.upper() #Convierte en Mayuscula
minusc = cadena2.lower () #Convierte en Minuscula
primer_letra_mayuscula = cadena2.capitalize #Convierte primer letra en mayuscula

busqueda_find = cadena1.find("e") #Busca cadena en otra cadena, si no hay coincidencias devuelve -1
print (busqueda_find)

busqueda_index = cadena1.index("2") #Misma funcion que con Find, pero lanza una Excepcion 

print (mayusc)


es_numerico = cadena1.isnumeric()
#Si es numerico devuelve True
es_alfanumerico = cadena1.isalpha
#Si es alfanumerico devuelve true





