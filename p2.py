print("")
print ("Zamarripa Castro Erick Fabián")
print("")

#Pide introducir una nota por encima de 4
n = float(input("Introduce la nota: "))
print("")

#Imprimira un mensaje dependiendo de la nota introducida por el usuario
if 0 <= n < 5:

    print("SUSPENSO")
    print("")
elif 5 <= n < 6:

    print("SUFICIENTE")
    print("")
elif 6 <= n < 7:

    print("BIEN")
    print("")
elif 7 <= n < 9:

    print("NOTABLE")
    print("")
elif 9 <= n <= 10:

    print("SOBRESALIENTE")
    print("")
else:

#Imprimira este mensaje al introducir un numero por encima de 10 o abajo de 5
    print("NOTA NO VÁLIDA")
print("")