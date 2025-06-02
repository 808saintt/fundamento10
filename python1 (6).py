import random

print("Bienvenido")
X = input("Agrega tu producto: ")

# Asegurémonos de que usamos una lista, no una tupla
lista = ["Pan", "Queso", X]  # Lista, no tupla
print("Su lista es: ", lista)

# Elegir aleatoriamente un producto que no está disponible
nodisponible = random.choice(lista)
print(f"Por favor modifique su compra, {nodisponible} No está disponible")

# Preguntar si desean eliminar el producto no disponible
print(f"Desea eliminar {nodisponible}?")
YN = input("Y o N: ")

if YN.lower() == "y":
    # Verificamos si el producto está en la lista antes de eliminarlo
    if nodisponible in lista:
        lista.remove(nodisponible)  # Elimina el producto de la lista
        print("Su lista final es: ", lista)
    else:
        print("El producto no estaba en la lista.")
elif YN.lower() == "n":
    print(f"{nodisponible} No está disponible, el sistema lo ha eliminado por defecto.")
    lista.remove(nodisponible)  # Elimina el producto de la lista
    print("Su lista final es: ", lista)
else:
    print("Respuesta no válida. El producto ha sido eliminado por defecto.")
    lista.remove(nodisponible)  # Elimina el producto de la lista
    print("Su lista final es: ", lista)
