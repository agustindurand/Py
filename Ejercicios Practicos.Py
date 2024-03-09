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
    
    
    
    
    
#Ver 10 horas de este curso a cuantas horas de otro curso equivale y ver las 10 horas de otros cursos a cuantas horas equivale de este curso