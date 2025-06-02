"""

def Suma(a, b):
    return a + b
Resultado = Suma(5, 7)
print("Resultado: ",Resultado)



a = input("Ingrese el primer número: ")
b = input("Ingrese el segundo número: ")    

def Suma(a, b):
    return a + b

Resultado = Suma(a, b)
print("Resultado: ",Resultado)
"""
"""
Pedir dos numeros a y b
limite inferior y superior
entre estos dos numeros sacar un numero aleatorio

a = input("Ingrese el primer número: ")
b = input("Ingrese el segundo número: ")    

import random as pene
resultado = pene.randint(int(a), int(b))
print("El número aleatorio entre ", a, " y ", b, " es: ", resultado)

operación=input("Desea SUMA o RESTA? (Esribalo en mayúsculas): ")
if operación=="SUMA":
    final = resultado + (resultado*0.10)
    print("El resultado de la suma es: ", final)
elif operación=="RESTA":
    final = resultado - (resultado*0.10)
    print("El resultado de la resta es: ", final)

else:
    print("Operación no válida")
"""
#
"""
La academia school of talent requiere realizar una aplicación en python, que les permita establecer el rango socioeconomico de cada uno de sus estudiantes, 
para poder proporcionar los distintos beneficios. 
Sabiendo que cada uno de los deciles establecidos, cuenta con una diferencia de 10% entre cada uno de ellos;
1. estrato mas bajo con calificacion de 7.0, beca 100%
2. estrato D con califiacion de 7.0, beca 40%
3. estrato C con calificacion de 7.0, beca 30%
4. estrato D con calificacion de 6.0, beca 30%
5. estrato B con calificacion de 6.0, beca 25%
6. estrato B con calificacion de 5.0, beca 20%
7. estrato A, beca 0%
El precio del curso es de 300.000 x 6 meses
"""
#

def calcular_beca(calificacion, estrato):
    # Precio del curso
    precio_curso = 300000 * 6  # 300.000 por 6 meses

    # Determinar el porcentaje de beca según la calificación y el estrato
    if estrato == "más bajo" and calificacion >= 7.0:
        beca = 100
    elif estrato == "D" and calificacion >= 7.0:
        beca = 40
    elif estrato == "C" and calificacion >= 7.0:
        beca = 30
    elif estrato == "D" and calificacion >= 6.0:
        beca = 30
    elif estrato == "B" and calificacion >= 6.0:
        beca = 25
    elif estrato == "B" and calificacion >= 5.0:
        beca = 20
    else:
        beca = 0

    # Calcular el precio final del curso después de aplicar la beca
    descuento = (beca / 100) * precio_curso
    precio_final = precio_curso - descuento

    return beca, precio_final


# Solicitar datos al usuario
calificacion = float(input("Ingrese la calificación del estudiante (0.0 - 10.0): "))
estrato = input("Ingrese el estrato socioeconómico del estudiante (más bajo, D, C, B, A): ")

# Calcular la beca y el precio final
beca, precio_final = calcular_beca(calificacion, estrato)

# Mostrar resultados
print(f"\nEl estudiante pertenece al estrato '{estrato}' con una calificación de {calificacion}.")
print(f"Porcentaje de beca asignado: {beca}%")
print(f"Precio final del curso después de aplicar la beca: ${precio_final:,.2f}")