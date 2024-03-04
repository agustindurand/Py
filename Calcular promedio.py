# 1. Definimos una función llamada 'calcular_promedio'
def calcular_promedio(lista):
    # 2. Si la lista está vacía, devolvemos 0
    if not lista:
        return 0
    # 3. Sumamos todos los elementos de la lista y los dividimos por la cantidad de elementos para obtener el promedio
    return sum(lista) / len(lista)

# 4. Creamos una lista de números
numeros = [2, 4, 6, 8, 10]

# 5. Llamamos a la función 'calcular_promedio' con nuestra lista y almacenamos el resultado en la variable 'promedio'
promedio = calcular_promedio(numeros)

# 6. Imprimimos el promedio
print("El promedio de los números es:", promedio)