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
        
        
