"""
Desarrolla un programa en Python que permita ingresar dos números enteros que indiquen un rango numérico. El primer valor debe ser menor que el segundo. El programa generará un número aleatorio dentro de ese rango. Luego, el usuario intentará adivinar el número generado en tres intentos.

    Si el usuario adivina en el primer intento, el programa mostrará el mensaje: "Felicitaciones, adivinaste en el primer intento."
    Si no acierta en el primer intento, el programa indicará si el número es mayor o menor que el intento del usuario.
    En el segundo intento, si el usuario no acierta, se volverá a indicar si el número es mayor o menor.
    Si el usuario no acierta en el tercer intento, el programa mostrará el mensaje: "Perdiste, el número era [número]."

"""

n1 = int(input("Ingrese el primer número: "))

n2 = int(input("Ingrese el segundo número: "))

while n2 < n1:
    n2=int(input("El segundo número debe ser mayor que el primero, ingrese un número válido: "))

import random

na = random.randint(n1,n2)

COUNT=0

while COUNT < 5:

    if COUNT == 0:
        spell="primer"
    if COUNT== 1:
        spell="segundo"
    if COUNT== 2:
        spell="tercer"

    print("Adivine el número entre ",n1," y ",n2)
    print("Ingrese su", spell ,"intento: ")
    TRY=int(input(""))

    if TRY < na:
        print("El número ",TRY," es menor que el número aleatorio.")
        COUNT=COUNT+1
    if TRY > na:
        print("El número ",TRY," es mayor que el número aleatorio.")
        COUNT=COUNT+1
    elif TRY == na:
        COUNT=COUNT+10
    else:
        print("")

if TRY==na:
    print("Felicidades usted ha acertado.")

if TRY!=na:
    print("No has acertado, más suerte a la próxima!.")