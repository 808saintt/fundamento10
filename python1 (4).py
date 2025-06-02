"""
El día de hoy necesito hacer la compra y hago la lista en python
primero un mensaje de bienvenida
agregar dos productos
print msg "añade tu producto" 
pedir modificar alguno de los prodcutos
eliminar uno de los productos
finalmente imprimir la lista final
"""

import random
print("Bienvenido")
X = input("Agrega tu producto ")
lista = [f"Pan","Queso",X]
print("Su lista es: ",lista)
nodisponible = random.choice(lista)
print("Por favor modifique su compra, ", nodisponible,"No está disponible")
print("Desea eliminar ",nodisponible,"?")
YN = input("Y o N ")

if YN.lower() == "y":
    if nodisponible in lista:
        lista.remove(nodisponible)  
        print("Su lista final es: ", lista)
    else:
        print("El producto no estaba en la lista.")
elif YN.lower() == "n":
    print(f"{nodisponible} No está disponible, el sistema lo ha eliminado por defecto.")
    lista.remove(nodisponible) 
    print("Su lista final es: ", lista)
else:
    print("Respuesta no válida. El producto ha sido eliminado por defecto.")
    lista.remove(nodisponible) 
    print("Su lista final es: ", lista)