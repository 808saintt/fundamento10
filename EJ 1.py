"""
El usuario debe ingresar un registro de temperatura entre 50 y -50 C°,
Dado que el usuario puede ingresar cualquier dato (incluso cadena de texto), Se puede usar manejo de excepción, para evitar que el programa se detenga.
1| Si el dato ingresado no es numero entero el programa debe printear: "Error: Debe ingresar un número entero válido.", repetir hasta que sea válido.
2| Si el usuario ingresa un numero entero fuera del rango; "Error: Temperatura fuera del rango permitido (-50°/50°)", repetir hasta solucionar.
3| Si el usuario ingresa correctamente los datos; "Temperatura registrada exitosamente."
4| Mostrar una opción para cerrar el programa, y si se selecciona mostrar: "Cerrando programa, hasta luego."
"""
exit = "1"
while exit != "si":

    class RangoTemperaturaError(Exception):
        pass

    while True:
        try:
            temp = int(input("Ingrese la temperatura: "))
            print(f"Usted ha ingresado una temperatura de {temp} °C")
            if not (-50<=temp<=50):
                raise RangoTemperaturaError
            break
        except ValueError:
            print("ERROR: El valor ingresado debe ser un número entero")
        except RangoTemperaturaError:
            print("Error: Temperatura fuera del rango permitido (-50°/50°)")


    print("Gracias por ingresar los datos!")
    
    exit = input("Ingrese (si), si desea salir del programa, o ingrese cualquier tecla para continuar: ")

