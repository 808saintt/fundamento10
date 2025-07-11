"""INFORMACIÓN DE USUARIOS

Al ingresar la opción 1: Se debe permitir ingresar el nombre del usuario, sexo y clave, por separado.,
Para que el ingreso del usuario sea exitoso, se debe compartir lo siguiente:
a) El nombre del usuario no debe estar repetido.
b) El sexo del usuario debe ser definido a travé de 2 letras: F o M.
c) La contraseña debe ser de un mínimo de 8 caracteres y al menos 1 número, sin espacios.
En caso de cumplir todas las funciones, el mensaje a mostrar en pantalla debe ser:
El ingreso fue exitoso.,
Al ingresar la opción 2: El menú debe permitir buscar usuarios mediante sus nombres. Si el usuario
existe, deben mostrarse los datos asociados al usuario, como lo son sexo y contraseña. Si el usuario
no existe, debe mostrar un mensaje: "El usuario no se encuentra."
Al ingresar la opción 3: El menú debe permitir borrar usuarios y toda la información asociada a este.
Al ingresar la opción 4: Preguntar si decide continuar buscando usuarios o salir del programa.
Si el ingreso de una opción distinta debe mostrar un mensaje que debe seleccionar una opción válida.
Todas las opciones del menú deben estar implementadas separadas del código principal (main():)"""


def ingresar_usuario():

  while True:

    user = input("Ingrese nombre de usuario: ")

    if user not in d:

      break

    else:

      print("Usuario ya existe. Intente otro.")

  while True:

    sex = input("Ingrese sexo (M/F): ")

    if sex == "M" or sex == "F":

      break

    else:

      print("Debe ingresar M o F solamente. Intente de nuevo.")

  while True:

    num = 0

    letra = 0

    passw = input("Ingrese contraseña: ")

    if len(passw) >= 8 and " " not in passw:

      for c in passw:

        if c.isdigit():

          num += 1

        if c.isalpha():

          letra += 1

      if num > 0 and letra > 0:

        print("Contraseña válida.")

        d[user] = [passw, sex]

        print("Usuario ingresado con éxito!!")

        break # <-- Esto es lo que faltaba

      else:

        print("La contraseña debe tener letras y números.")

    else:

      print("Contraseña no válida. Debe tener al menos 8 caracteres y sin espacios.")



def buscar_usuario(user):

  if user in d:

    print("El sexo del usuario es:", d[user][1], "y la contraseña es:", d[user][0])

  else:

    print("El usuario no se encuentra.")



def eliminar_usuario(user):

  if user in d:

    del d[user]

    print("Usuario eliminado correctamente.")

  else:

    print("No se pudo eliminar. El usuario no existe.")



### MAIN

d = {}

while True:

  print("\nMENU PRINCIPAL")

  print("1.- Ingresar usuario.")

  print("2.- Buscar usuario.")

  print("3.- Eliminar usuario.")

  print("4.- Salir.")

  op = input("Ingrese opción: ")

  if op == "4":

    print("Programa terminado...")

    break

  elif op == "1":

    ingresar_usuario()

  elif op == "2":

    usuario = input("Ingrese usuario a buscar: ")

    buscar_usuario(usuario)

  elif op == "3":

    usuario = input("Ingrese usuario a eliminar: ")

    eliminar_usuario(usuario)

  else:

    print("Debe ingresar una opción válida!!")