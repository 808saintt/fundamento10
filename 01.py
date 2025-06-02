with open ("datos.txt", "w") as archivo:
    archivo.write("Nombre: Maria\n")
    archivo.write("Edad: 26\n")
    archivo.write("Carrera: Ing \n")
#########################################
try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
except FileExistsError as error:
    print("El archivo no existe", error)
else:
    print("Archivo existoso.")
finally:
    print("Gracias por usar el programa")

