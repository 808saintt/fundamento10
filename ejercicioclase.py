"""
Desarrolle un programa en Python que permita calcular el subsidio de gas según el quintil
de ingreso al que pertenece la familia del solicitante y sus condiciones laborales.
Condiciones socioeconómicas:
Menor Ingreso
Mayor Ingreso
Condiciones laborales:
Se considera si la persona está empleada o desempleada.
Condiciones de subsidio:
Gas
Quintil: 1 o 2, Laboral: Desempleado, Subsidio: 10.000
Quintil: 1 o 2, Laboral: Empleado, Subsidio: 8.000
Quintil: 3, Laboral: Desempleado, Subsidio: 6.000
Quintil: 3, Laboral: Empleado, Subsidio: 4.000
Quintil: 4 o 5, Laboral: Cualquiera, Subsidio: 1.500
Bonos adicionales:
Si la persona pertenece al quintil 1 o 2, recibe un bono de 2.000, y si tiene más de 65 años, recibe un bono de 3.000.
"""
print ("Bienvenido, este es un programa de subsidio al gasto de gas")
print ("recuerde escribir su numero de quintil(Ej: 1, 2, 3, 4, 5)")
condicion_lab = "pene"
quintil = 6
while (quintil <1 or quintil >5) or (condicion_lab != "empleado" or "desempleado"):
                                    
   
    quintil = int(input ("Cual es su quintil(1 a 5)? "))
    condicion_lab = input ("Cual es su condicion laboral? (empleado, desempleado) ")
    subsidio = 0

    if (quintil == 1 or quintil == 2) and (condicion_lab == "desempleado" ):
        subsidio = 10000
        print ("su subsidio es de " ,subsidio)
    if (quintil == 1 or quintil == 2) and (condicion_lab == "empleado" ):
        subsidio = 8000
        print ("su subsidio es de " ,subsidio)
    if (quintil == 3) and (condicion_lab == "desempleado" ):
        subsidio = 6000
        print ("su subsidio es de " ,subsidio)
    if (quintil == 3) and (condicion_lab == "empleado" ):
        subsidio = 4000
        print ("su subsidio es de " ,subsidio)
    if (quintil == 4 or quintil == 5) and (condicion_lab == "desempleado" or "empleado" ):
        subsidio = 1500
        print ("su subsidio es de " ,subsidio) 

    if (quintil <1 or quintil >5) :
        print("error, tiene que seleccionar un numero del 1 al 5" )
    elif (condicion_lab !="empleado" or "desempleado"):
        print("tiene que seleccionar una condicion laboral valida")

edad =int(input("Ingrese su edad "))
if edad >=65 :
    subsidio = subsidio + 3000
    print ("por tener arriba de 65 años se le dara un bono extra de 3000, en total su subsidio es de: " ,subsidio)

if (quintil == 1 or quintil == 2):
    subsidio = subsidio + 2000
    print ("por ser del quintil 1 o 2, se le da un bono adicional de 2000, su subsidio total es de:" ,subsidio)   
 

