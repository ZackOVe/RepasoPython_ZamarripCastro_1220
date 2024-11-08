print("")
print ("Zamarripa Castro Erick Fabián")
print("")

#Declara el nombre y apellido a usar
nombre = "Daniel"
apellido = "Ramos"

#Captura el nombre y apellido del usuario
nombre_input = input("Introduce el nombre: ")
print("")
apellido_input = input("Introduce el apellido: ")
print("")

#Comprobamos si el nombre y apellido son correctos
if nombre_input == nombre:
    
    if apellido_input == apellido:
        print("Nombre y apellido correctos")
        print("")
    else:
        print("Apellido incorrecto")
        print("")
else:
    print("Usuario desconocido")
    print("")


