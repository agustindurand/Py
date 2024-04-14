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