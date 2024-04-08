#El tiempo promedio de visualizacion de un curso en video es de 2,5 horas como minimo, 7 horas como maximo y 4 horas en promedio, este curso se visualizo en una hora y media, A) Cuanta diferencia hay en porcentaje entre el curso actual y el mas rapido de otros cursos, el mas lento de otros cursos y el promedio de los cursos
    
duracion_cursos_tiempo_minimo = 2.5
duracion_cursos_tiempo_maximo = 7
promedio_tiempo_cursos = 4
tiempo_curso_actual = 1.5


    
    #Diferencias
      
diferencia_con_el_curso_tiempo_minimo = 100 - tiempo_curso_actual / duracion_cursos_tiempo_minimo * 100 
diferencia_con_el_curso_tiempo_maximo = 100 - tiempo_curso_actual * 1000 // duracion_cursos_tiempo_maximo /10
diferencia_con_promedio = 100 - tiempo_curso_actual / promedio_tiempo_cursos * 100

print (f"El curso actual dura un {diferencia_con_el_curso_tiempo_minimo} % menos que el mas rapido")    
print (f"El curso actual dura un {diferencia_con_el_curso_tiempo_maximo} % menos que el mas lento")
print (f"El curso actual dura un {diferencia_con_promedio} % menos que el mas promedio")
    
    
    
#B. Teniendo en cuenta que la cantidad de crudo en promedio es de 5 horas, y se reduce a 4 horas con la edicion, y teniendo en cuenta que el crudo de este video es de 3 horas y media y con la edicion se redujo a una hora y media. Que porcentaje de material inservable se reduce del crudo en ambos casos
    
  
crudo_promedio = 5 
crudo_actual = 3 

tiempo_vacio_removido_curso_actual =    100 - (tiempo_curso_actual * 1000// crudo_actual / 10)
tiempo_vacio_removido = 100 - (promedio_tiempo_cursos * 1000) // crudo_promedio / 10 

print(f"Un curso promedio elimina un {tiempo_vacio_removido}% de tiempo")
print(f"El curso actual elimino un {tiempo_vacio_removido_curso_actual}& de tiempo vacio")
    
#Ver 10 horas de este curso a cuantas horas de otro curso equivale y ver las 10 horas de otros cursos a cuantas horas equivale de este curso

print(f"Ver 10 horas de este curso equivale a ver {promedio_tiempo_cursos * 100 // tiempo_curso_actual / 10} horas de otros curso" )



#Ejercicio 2.
# Hoy falto el profesor de clases, y los chicos se organizaron para armar su clase, un alumno es el profesor y el otro es el asistente. 
#A) Solicitar la edad de los compañeros que asistieron a clase y ordenar datos de mayor a menos 
#B) El mayor de la clase es el profesor y el menor es el asistente, ¿Quien es quien?


def obtener_compañeros (cantidad): #Declaracion de funcion con argumento 
    compañeros = []                #Se crea una lista vacia llamada Compañeros la cual va a almacenar nombres y edades 
    for i in range(cantidad):      #Bucle for que se va a iterar la cantidad de veces que sea el numero del argumento 
        nombre = input("Ingrese el nombre del compañero: ") #Dentro del bucle, se solicita al usuario que ingrese el nombre y la edad de cada compañero. El nombre se guarda en la variable nombre y la edad se guarda en la variable edad
        edad = int(input("Ingrese la edad del compañero: "))
        compañero = (nombre,edad) #Creacion de Tupla con los valores ingresados en esas variables
        compañeros.append(compañero) #Con append agrego un elemento en ultima posicion a una lista, en este caso a lista compañeros
        compañeros.sort(key=lambda x:x[1]) #Ordena de Mayor a menor segun la edad, con el metodo .Sort 
        asistente = compañeros [0][0]
        profesor = compañeros [-1][0]
        
    return asistente, profesor
    
asistente, profesor = obtener_compañeros (19)

print(f"El profesor es: {profesor} y el asistente es {asistente}")

#Crear funcion que al pasarle un numero, genere numero primo hasta llegar a ese numero 

