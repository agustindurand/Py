""" 00 EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!" 
 """ 

#Comentario de insercion de URL https://www.python.org/
#Comentario Modo Ejemplo Numero 1 
""""Comentario Modo Ejemplo
    Numero 2"""
Variable = True
Variable2 = 1,5
Variable3 = "String"
Variable4 = 100 
Variable5 = False
CONSTANTE_NRO1 = 120
print("Hello Python")

print(type(Variable))
print(type(Variable2))
print(type(Variable3))
print(type(Variable4))
print(type(Variable5))


""""
 * 01 EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */  """ 
 
 
 
#Operadores Aritméticos:

numero_ejemplo = 12 
numero_ejemplo2 = 14

numero_ejemplo + numero_ejemplo2
numero_ejemplo - numero_ejemplo2
numero_ejemplo * numero_ejemplo2
numero_ejemplo / numero_ejemplo2
numero_ejemplo % numero_ejemplo2
numero_ejemplo ** numero_ejemplo2
numero_ejemplo // numero_ejemplo2

# Operadores Lógicos:

numero_ejemplo > 10 and numero_ejemplo2 > 10 
numero_ejemplo < 10 or numero_ejemplo2 < 10 
resultado = not (numero_ejemplo < numero_ejemplo2)



numero_ejemplo == numero_ejemplo2 #False
numero_ejemplo != numero_ejemplo2 #True

numero_ejemplo >= numero_ejemplo2 
numero_ejemplo <= numero_ejemplo2


#Operadores de Asignación:

numero_ejemplo3 = 12000
numero_ejemplo3 += numero_ejemplo
numero_ejemplo2 -= numero_ejemplo 
numero_ejemplo2 *= numero_ejemplo
numero_ejemplo2 /= numero_ejemplo

#Operadores de Identidad:

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista1 is lista2 #False
lista1 is not lista2 

#Operadores de Pertenencia:

tupla = ("elemento1", "elemento2", "elemento3", "elemento4")
"elemento3" in tupla #True 

"elemento5" not in tupla #True 
 
#Estructuras de Control Condicional
numero_condicional = 10
if numero_condicional > 0:
    print("El número es positivo.")
elif numero_condicional < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")


#Estructura de Control Iterativa

for i in range(1, 10): #la variable i se declara simultaneamente a la declaracion del For
    print(f"Este es el número que se obtiene mediante la estructura de control Iterativa For {i}")
    
contador = 0
while contador < 5:
    print(f"El contador es: {contador}")
    contador += 1
    
for x in range(1, 11):
    if x == 5:
        continue  # Salta la iteración actual si el número es 5
    elif x == 8:
        break  # Sale del bucle si el número es 8
    else:
        pass  # No hace nada, solo pasa al siguiente paso
    print(f"Impresion de numero con estructura Continue, Break y Pass {x}")


#No hay Switch en Python 

#EJERCICIO
for numero_ejercicio in range (10,55):
    if numero_ejercicio % 2 == 0 and numero_ejercicio != 16 and numero_ejercicio % 3 != 0:
        print(numero_ejercicio)
        
        
""""
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */
  """
  
def Welcome(): #Declaracion de Funcion
    print("Welcome") #Contenido de Funcion, unicame realiza una impresion en consola
Welcome() #Invocacion de la Funcion

def cuadrado(x): #Declaracion de Funcion que recibe un parametro
    return x ** 2 #Retorna el resultado de la elevacion del parametro al cuadrado
resultado = cuadrado(5) #Se asigna valor a una variable, invocando a la funcion con un parametro indicado, en este caso 5
print("El cuadrado de 5 es:", resultado) #Impresion de la variable (Por fuera de la funcion)

def suma(z, x): #Declaracion de Funcion que recibe dos parametros
    return z + x #Retorna el resultado de la suma de los dos parametros
resultado = suma(144, 144) #Se asigna valor a la variable, invocando a la funcion con los parametros indicados, en este caso 144 y 144
print("La suma de 144 y 144 es:", resultado) #Impresion de la variable

def exterior(): #Declaracion de Funcion con otra funcion dentro suyo
    def interior(): #Funcion interior dentro del cuerpo de otra funcion 
        print("¡Función interior ejecutada!") 
    print("Ejecutando la función exterior.")
    interior()
exterior()


variable_global = 10 #Declaracion de Variable Global
def funcion_comprueba_variable_global(): #Declaracion de funcion 
    variable_local = 5 #Declaracion de Variable Local
    print("Variable local dentro de la función:", variable_local)
    print("Variable global dentro de la función:", variable_global)
funcion_comprueba_variable_global() #Invocacion a Funcion
print("Variable global fuera de la función:", variable_global)

cuadrado = lambda x: x ** 2 #Funcion Lambda 
print("El cuadrado de 4 es:", cuadrado(4))


#EJERCICIO 

def funcion_retorna_numeros (a,b):
    contador = 0 
    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(f"El {numero}, En este caso es multiplo de 3 y de 5 el numero: {a} y del {b}")
    
        elif numero % 3 == 0:
            print(f"El {numero}, En este caso, el numero es multiplo de 3: {a}")
         
        elif numero % 5 == 0:
            print (f"El {numero}, En este caso, el numero es multiplo de 5: {b}")   
            
        else:
            print(f"{numero}No es ni multiplo de 3 ni de 5.")
        contador += 1
            
    return contador
  
contador = funcion_retorna_numeros("Ventaja del 3", "Ventaja del 5")
print("Número de veces que se ha impreso el número:", contador)

"""" 
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */
 
 """
# Lista vacía
lista_vacia = []

# Lista con elementos
mi_lista = [1, 2, 3, 4, 5]

# Lista de listas (matriz)
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]



#Inserción
# Agregar un elemento al final de la lista
mi_lista.append(6)

# Insertar un elemento en una posición específica
mi_lista.insert(0, 0)

#Borrado
# Eliminar el último elemento de la lista
ultimo_elemento = mi_lista.pop()

# Eliminar un elemento en una posición específica
elemento_eliminado = mi_lista.pop(0)

# Eliminar un elemento por valor
mi_lista.remove(3)

#Actualización:

# Actualizar un elemento en una posición específica
mi_lista[0] = 10

#Ordenación
# Ordenar la lista en su lugar (ascendente)
mi_lista.sort()

# Ordenar la lista en su lugar (descendente)
mi_lista.sort(reverse=True)

# Crear una nueva lista ordenada (ascendente)
lista_ordenada = sorted(mi_lista)

# Crear una nueva lista ordenada (descendente)
lista_ordenada_desc = sorted(mi_lista, reverse=True)


#TUPLAS --> INMUTABLES
# Tupla vacía
tupla_vacia = ()

# Tupla con elementos
mi_tupla = (1, 2, 3, 4, 5)



# Conjunto vacío (sets)
conjunto_vacio = set()

# Conjunto con elementos
mi_conjunto = {1, 2, 3, 4, 5}

#Inserción 
# Añadir un elemento
mi_conjunto.add(6)

# Añadir múltiples elementos
mi_conjunto.update({7, 8, 9})

#Borrado
# Eliminar un elemento
mi_conjunto.remove(3)






# Diccionario vacío
diccionario_vacio = {}

# Diccionario con elementos
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
#Inserción 
# Agregar un nuevo par clave-valor
mi_diccionario['d'] = 4


#Borrado 
# Eliminar un par clave-valor
del mi_diccionario['a']

# Eliminar un par clave-valor y devolver el valor
valor_eliminado = mi_diccionario.pop('b')


#Actualización
# Actualizar el valor de una clave existente
mi_diccionario['c'] = 10

"""" 
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */ """ 
 
 
diccionario_agenda = {
    "Stacy": 1123432219,
    "Klaus": 1166544321,
    "Chinese": 1222334321,
    "Doctor": 1199897621,
    "Drago" : 1128281723
}
def mostrar_contactos (diccionario_agenda):
    print("La lista de contactos actual es la siguiente:")
    # Ordenar las claves del diccionario (nombres) alfabéticamente
    for nombre in sorted(diccionario_agenda.keys()):
        telefono = diccionario_agenda[nombre]  # Obtener el número de teléfono del nombre
        print(f"{nombre}: {telefono}")
def insertar_contacto(diccionario_agenda): 
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono del contacto: ")

    # Verifica si el número de teléfono tiene solo dígitos y no tiene más de 11 dígitos
    if telefono.isdigit() and len(telefono) <= 11:
        # Verificar si el nombre no está en el diccionario
        if nombre not in diccionario_agenda:
            diccionario_agenda[nombre] = telefono
            print("Contacto agregado exitosamente.")
        else:
            print("El contacto ya existe en la agenda.")
    else:
        print("El número de teléfono debe contener solo dígitos numericos y tener como máximo 11 caracteres.")
def actualizar_contacto(diccionario_agenda):
    nombre = input("Ingrese el nombre del contacto que desea actualizar: ")
    if nombre in diccionario_agenda:
        telefono = input("Ingrese el nuevo número de teléfono: ")

        # Verificar si el número de teléfono es numérico y tiene la longitud adecuada
        if telefono.isdigit() and len(telefono) <= 11:  # Se puede ajustar la longitud según sea necesario
            diccionario_agenda[nombre] = telefono
            print(f"El contacto '{nombre}' ha sido actualizado correctamente.")
        else:
            print("El número de teléfono ingresado no es válido.")
    else:
        print(f"No se encontró el contacto '{nombre}' en la agenda.")
def eliminar_contacto(diccionario_agenda): 
    contacto_para_eliminar = input("Ingrese el nombre del contacto que desea Eliminar: ") #Solicita a Usuario contacto para borrar
    contacto_para_eliminar = contacto_para_eliminar.lower()  # Convierte a minusculas el nombre ingresado por el usuario 
    
    
    diccionario_agenda_minusculas = {key.lower():value for key, value in diccionario_agenda.items()}
    #crea un nuevo diccionario. Para cada par clave-valor en el diccionario original, toma la clave y la convierte a minúsculas, luego asigna esta clave en minúsculas al valor correspondiente en el nuevo diccionario
    
    if contacto_para_eliminar in diccionario_agenda_minusculas: #Comprueba si el nombre del contacto (en minúsculas) está presente como clave en el diccionario diccionario_agenda_minusculas
        nombre_real = next(key for key, value in diccionario_agenda.items() if key.lower() == contacto_para_eliminar)
        eliminado = diccionario_agenda.pop(nombre_real)
        print(f"El contacto '{nombre_real}' ha sido borrado exitosamente")
    else:
        print("No se han encontrado coincidencias")   
def buscar_contacto(diccionario_agenda): #Recibe parametro el diccionario anteriormente declarado
    eleccion_usuario = input("Ingrese un dígito numerico, letra o nombre completo para buscar contactos: ") #Solicitamos al usuario que ingrese   
    resultado_busqueda_contactos = False  #Variable booleana declarada 

    for nombre, telefono in diccionario_agenda.items(): #Bucle que itera sobre todos los elementos del diccionario por el metodo .items a cada clave-valor del diccionario, se le asigna variable nombre y telefono 
        if eleccion_usuario in str(telefono): #Verifica si el digito colocado por el usuario se encuentra el valor de alguno de los telefonos 
            print(f"El contacto puede ser: {nombre} - {telefono}")
            resultado_busqueda_contactos = True 
        else:  # Si la entrada del usuario no es un dígito numérico
            if eleccion_usuario.lower() in nombre.lower() or nombre.lower().startswith(eleccion_usuario.lower()):
                print(f"{nombre}: {telefono}")
                resultado_busqueda_contactos = True 

    if not resultado_busqueda_contactos: 
        print("No se encontraron coincidencias.")
def opciones_agenda():
    funciones = {
        1: buscar_contacto,
        2: insertar_contacto,
        3: actualizar_contacto,
        4: eliminar_contacto,
        5: mostrar_contactos
    }
    while True:
        print("\nSeleccione una opción:")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Mostrar Contactos")
        print("6. Cerrar agenda ")
        numero_usuario = input("Ingrese un número para seleccionar una opción: ")

        if numero_usuario.isdigit():
            numero_usuario = int(numero_usuario)
            if numero_usuario == 6:
                confirmacion = input("¿Está seguro de cerrar la agenda? (si/no): ")
                if confirmacion.lower() == "si":
                    print("Cerrando la agenda...")
                    break
                elif confirmacion.lower() == "no":
                    print("Continuando en el sistema...")
                else:
                    print("Respuesta no válida. Por favor, responda 'si' o 'no'.")
            elif numero_usuario in funciones:
                funciones[numero_usuario](diccionario_agenda)
            else:
                print("Número de función no válido.")
        else:
            print("Por favor, ingrese un número válido.")

opciones_agenda()


"""
EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación... """
 
cadena_acceder_caracter = "I am Work in Python"
tercer_caracter = cadena_acceder_caracter[3]  
print(tercer_caracter) 



subcadena = cadena_acceder_caracter[1:5]  
print(subcadena) 


longitud = len(cadena_acceder_caracter)
print(longitud) 


otra_cadena = "¡Hello!"
concatenada = cadena_acceder_caracter + " " + otra_cadena
print(concatenada)  


repetida = otra_cadena * 3
print(repetida) 


for caracter in cadena_acceder_caracter:
    print(caracter)


mayusculas = cadena_acceder_caracter.upper()
print(mayusculas)  

minusculas = cadena_acceder_caracter.lower()
print(minusculas)  # Output: 'hola mundo'


reemplazada = cadena_acceder_caracter.replace("Python", "Js")
print(reemplazada)  


palabras = cadena_acceder_caracter.split()
print(palabras) 


palabras = ['Hola', 'mundo']
unida = ' '.join(palabras)
print(unida)  # Output: 'Hola mundo'



"""" 
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */
"""
 
def es_palindromo(palabra):
    palabra = palabra.lower()
    return list(palabra) == list(reversed(palabra))

def son_anagramas(palabra1, palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    return sorted(palabra1) == sorted(palabra2)

def es_isograma(palabra):
    palabra = palabra.lower()
    letras_unicas = set(palabra)
    return len(letras_unicas) == len(palabra)

def detector_palabras(palabra1, palabra2):
    if es_palindromo(palabra1) and es_palindromo(palabra2):
        print("Ambas palabras son palíndromos.")
    elif son_anagramas(palabra1, palabra2):
        print("Las palabras son anagramas.")
    elif es_isograma(palabra1) and es_isograma(palabra2):
        print("Ninguna palabra es un palíndromo o un anagrama, pero ambas son isogramas.")
    else:
        print("Las palabras no son palíndromos, anagramas ni isogramas.")

# Ejemplo de uso
palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")
detector_palabras(palabra1, palabra2)