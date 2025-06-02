with open("datos03.txt", "a") as archivo:
    Cantidad = int(input("Indica cuantos estudiantes desea ingresar: "))

    for i in range(Cantidad):
        print(f"\nIngresa datos del estudiante {i+1}")
        nombre = input("Nombre: ")
        edad = input ("Edad: ")
        carrera = input ("Carrera: ")
        promedio = input ("Promedio: ")

        archivo.write(f"|ESTUDIANTE {i+1}:\n")
        archivo.write(f"Nombre {nombre}:\n")
        archivo.write(f"Edad {edad}:\n")
        archivo.write(f"Carrera {carrera}:\n")
        archivo.write(f"Promedio {promedio}:\n")
