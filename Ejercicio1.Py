#El índice de masa corporal (IMC) es una medida que se utiliza para determinar si una persona tiene un peso saludable para su altura. La fórmula para calcular el IMC es: IMC = peso (kg) / (altura (m) * altura (m)), Escribe un programa en Python que solicite al usuario su peso (en kilogramos) y su altura (en metros), y luego calcule e imprima su IMC.

altura = float (input("Ingrese su altura:  "))
peso = float (input("Ingrese su peso:  "))
IMC = peso / (altura**2)

print (f"Su IMC es {IMC}")

#Supongamos que estás trabajando en un equipo de desarrollo de software y te han asignado la tarea de crear una función en Python para validar contraseñas. La función debe cumplir con los siguientes requisitos: 
# La contraseña debe tener al menos 8 caracteres de longitud.
# La contraseña debe contener al menos una letra mayúscula.
# La contraseña debe contener al menos una letra minúscula.
# La contraseña debe contener al menos un número.
# Tu tarea es escribir una función llamada validar_contrasena que tome una contraseña como argumento y devuelva True si la contraseña cumple con todos los requisitos mencionados anteriormente, o False si no.

def validar_contrasena(contrasena):
    # Verificar la longitud de la contraseña
    if len(contrasena) < 8:
        return False

    # Verificar si hay al menos una letra mayúscula
    if not any(caracter.isupper() for caracter in contrasena):
        return False

    # Verificar si hay al menos una letra minúscula
    if not any(caracter.islower() for caracter in contrasena):
        return False

    # Verificar si hay al menos un número
    if not any(caracter.isdigit() for caracter in contrasena):
        return False

    # Si la contraseña pasa todas las verificaciones, retornar True
    return True

# Ejemplo de uso de la función
contrasena = input("Ingrese su contraseña: ")
if validar_contrasena(contrasena):
    print("La contraseña es válida.")
else:
    print("La contraseña no es válida.")