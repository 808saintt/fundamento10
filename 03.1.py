def obtener_ultimo_numero_estudiante(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                if linea.startswith("|ESTUDIANTE"):
                    partes = linea.split()
                    try:
                        ultimo_numero = int(partes[1][:-1]) 
                    except ValueError:
                        ultimo_numero = 0
            else:
                return ultimo_numero if 'ultimo_numero' in locals() else 0
    except FileNotFoundError:
        return 0

nombre_archivo = "datos03.txt"
ultimo_numero = obtener_ultimo_numero_estudiante(nombre_archivo)
conteo_inicial = ultimo_numero + 1

with open(nombre_archivo, "a") as archivo:
    Cantidad = int(input("Indica cuantos estudiantes desea ingresar: "))

    for i in range(Cantidad):
        print(f"\nIngresa datos del estudiante {conteo_inicial + i}")
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        carrera = input("Carrera: ")
        promedio = input("Promedio: ")

        archivo.write(f"|ESTUDIANTE {conteo_inicial + i}:\n")
        archivo.write(f"Nombre: {nombre}\n")
        archivo.write(f"Edad: {edad}\n")
        archivo.write(f"Carrera: {carrera}\n")
        archivo.write(f"Promedio: {promedio}\n")