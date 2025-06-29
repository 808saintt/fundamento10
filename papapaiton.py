# Variables globales
stock = {1: 50, 2: 50}
entradas = {}  # clave: nombre comprador, valor: show comprado

def venta_entradas():
    global stock, entradas
    nombre = input("Ingrese el nombre del comprador: ").strip()
    if nombre in entradas:
        print("ERROR: Este comprador ya tiene una entrada registrada.")
        return

    print("Seleccione el show:\n1- movimientos originales con la tripulación\n2- movimientos originales con sonrisa")
    try:
        opcion_show = int(input("Ingrese opción (1 o 2): "))
        if opcion_show not in [1, 2]:
            print("Opción inválida.")
            return
        if stock[opcion_show] == 0:
            print("No quedan entradas para este show.")
            return
        entradas[nombre] = opcion_show
        stock[opcion_show] -= 1
        print(f"Compra exitosa. {stock[opcion_show]} entradas restantes para el show {opcion_show}.")
    except ValueError:
        print("Entrada inválida. Debe ingresar un número.")

def cambiar_show():
    global stock, entradas
    nombre = input("Ingrese el nombre del comprador para el cambio: ").strip()
    if nombre not in entradas:
        print("No se encontró ese comprador.")
        return

    show_actual = entradas[nombre]
    show_nuevo = 1 if show_actual == 2 else 2

    if stock[show_nuevo] == 0:
        print("No hay stock disponible para el show al que desea cambiarse.")
        return

    stock[show_actual] += 1
    stock[show_nuevo] -= 1
    entradas[nombre] = show_nuevo
    print(f"Cambio exitoso a show {show_nuevo}. Stock actualizado.")

def mostrar_stock():
    print(f"Entradas disponibles:\nShow 1: {stock[1]} entradas\nShow 2: {stock[2]} entradas")

def main():
    while True:
        print("\n--- Menú Principal ---")
        print("1- Ventas de entradas")
        print("2- Cambio de show")
        print("3- Mostrar stock de funciones")
        print("4- Salir del programa")

        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                venta_entradas()
            elif opcion == 2:
                cambiar_show()
            elif opcion == 3:
                mostrar_stock()
            elif opcion == 4:
                print("Saliendo del sistema. ¡Gracias!")
                break
            else:
                print("Opción inválida. Ingrese un número entre 1 y 4.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")

if __name__ == "__main__":
    main()
