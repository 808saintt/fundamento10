"""Desarrolla un programa en Python que permita ingresar dos números enteros 
que indiquen un rango numérico.
 El primer valor debe ser menor que el segundo.
   El programa generará un número aleatorio dentro de ese rango. 
   Luego, el usuario intentará adivinar el número generado en tres intentos.

Si el usuario adivina en el primer intento, el programa mostrará el mensaje: 
"Felicitaciones, adivinaste en el primer intento."
Si no acierta en el primer intento,
 el programa indicará si el número es mayor o menor que el intento del usuario.
En el segundo intento, si el usuario no acierta, se volverá a indicar si el número es mayor o menor.
Si el usuario no acierta en el tercer intento, el programa mostrará el mensaje: 
"Perdiste, el número era [número]."""

import random
N1 = int(input("Indique un numero: "))

N2 = int(input("Indique un numero: "))


while N2<N1:
  N2 = input ("Ingrese el numero nuevamente(mayor que el primer digito ingresado)")

RN = random.randint(N1, N2)
print (RN)
COUNT = 0
while COUNT <3:

  intento=int(input("Ingrese su intento por adivinar "))

  if intento > RN:
    print("su numero es mayor al numero aleatorio ")
    COUNT = COUNT+1
  if intento < RN:
    print("su numero es menor al numero aleatorio ")
    COUNT = COUNT+1
  if intento == RN:
    if COUNT == 0: 
      print ("Felicidades, lo ha adivinado al primer intento ")
    if COUNT == 1: 
      print ("Felicidades, lo ha conseguido al segundo intento")
    if COUNT == 2: 
      print ("Felicidades, lo ha conseguido al tercer intento")
    COUNT = COUNT+3
#########################

if COUNT != RN:
    print("Se le han acabado los intentos, el numero correcto era" ,RN)


    
    












