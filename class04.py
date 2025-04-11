#hacer la compra, lista en python, primer mensaje(Bienvenida)
#agregar dos productos, mensaje(añade tu producto)
#solicitar al usuario modificar el producto
#eliminar alguno de los productos
#imprimir lista de resultados

import random
print ("Bienvenido, tu lista es: ")
x = input("agrega tu producto: ")
list =(f"Brazo de reina" , "  torta de mil hojas", x)
print ("su lista es: ", list)
NoDisponible = random.choice(list)
print("Por favor modifique su compra, " , NoDisponible, "No Esta disponible")
print("desea eliminar ",NoDisponible, "?")


