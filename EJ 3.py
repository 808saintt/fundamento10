"""
Construya un programa de python que permita gestionar un sistema simple para una fonda.
Debe presentar al usuario los siguientes productos:
"""
A="""
INGRESE  EL  NÚMERO  DE  LO  QUE  DESEE
1|Empanadas de pino________________2000
2|Empanadas de queso_______________1500
3|Choripan_________________________2500
4|Terremoto________________________1000

Ingrese su elección: 
"""
"""
|-----------------------------------------------------------------------------|
| Por su compra mayor a diezmil pesos, recibe un descuento del 25%,           |
| Por una compra mayor a veintemil, recibe un descuento del 40%,              |
| Y finalmente por su compra mayor a las otras dos, las entradas salen gratis |
| (el profe no dijo cuanto valen las entradas asi que digamos que 5000)       |
| (el profe hizo los rangos como el pene asi que mayor a 30k es gratis)       |
|-----------------------------------------------------------------------------|

"""

print("Bienvenido a la fonda punta peuco")

pino = 0
queso = 0
choripan = 0
terre = 0
quantity = 0
out = 0

#SELECCION DE COMIDA#

while out != 1:

    elect = int(input(A))


    match elect:
        case 1:
            print("|Usted ha seleccionado empanadas de pino|")
            quantity = int(input("¿Cuántas desea?: "))
            pino = pino + quantity
            print(f"Usted ha escogido {pino} empanadas de pino.")
            
        case 2:
            print("|Usted ha seleccionado empanadas de queso|")
            quantity = int(input("¿Cuántas desea?: "))
            queso = queso + quantity
            print(f"Usted ha escogido {queso} empanadas de queso.")

        case 3:
            print("|Usted ha seleccionado choripan|")
            quantity = int(input("¿Cuontas desea?: "))
            choripan = choripan + quantity
            print(f"Usted ha escogido {choripan} choripanes.")

        case 4:
            print("|Usted ha seleccionado Terremoto|")
            quantity = int(input("¿Cuántos desea?: "))
            terre = terre + quantity
            print(f"Usted ha escogido {terre} terremotos")
        case _:
            print("Escoja una opción válida.")


    print("")
    print("Ingrese [si] o [no]")
    exit = input("¿Desea realizar otra operación?: ")

    if exit == "si":
        out = 0
    elif exit == "no":
        out = 1
    else:
        while exit != 1 or 0:
            print("Por favor ingrese una opción válida: [si] o [no]")
            exit = input("¿Desea realizar otra operación?")
            if exit == "si":
                out = 1
            elif exit == "no":
                out = 0

#TOTAL DE LA COMPRA#

print("")
print("En total usted ha escogido:")
print(f"-{pino} empanadas de pino.")
print(f"-{queso} empanadas de queso.")
print(f"-{choripan} choripanes.")
print(f"-{terre} terremotos")
total = (pino*2000) + (queso*1500) + (choripan*2500) + (terre*1000)
print(f"Por lo que en total va a pagar ${total}")

if total >= 10000 and total < 20000:
    print("Además usted tiene un descuento del 25 porciento en la entrada ")
if total >= 20000 and total < 30000:
    print("Además usted tiene un descuento del 40 porciento en la entrada")
if total >= 30000:
    print("Además usted tiene un descuento del 100 porciento en la entrada")

#END#

print("Gracias por escojer la fonda punta peuco.")
print("Recuerde canjear su descuento en boletería con la boleta de esta compra :)")