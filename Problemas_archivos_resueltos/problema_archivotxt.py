
 #Partiendo de dos listas, las cuales contienen datos de nombres y apellidos de distintos usuarios, 
 
names = ["Sofía", "Martín", "Alejandro", "Camila", "Sebastián", "Isabella", "Nombre", "Mateo"]
last_name = ["García", "Rodríguez", "Martínez", "López", "González", "Pérez", "Sánchez", "Romero" ]

#Registrar dicha informacion en un archivo TXT

with open ("nombres_y_apellidos.txt","w", encoding="UTF-8") as arch: 
    arch.writelines("Los datos son: \n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n-----------------\n") for n,a in zip(names,last_name)]