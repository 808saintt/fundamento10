"""los dueños del vivero san joaquin necesitan realizar un programa en python, para ello cuentan con su talento Como desarolladores
cuyo programa le va a colaborar en el inventario y venta de las plantas, a continuacion menciono 10 de los productos mas vendidos"""



A="""1-Rosas blancas:Excelente para esta primavera:                                                           -2000 pesos
2-Mata de navidad:Planta para recordar el milagro de la navidad:                                         -5000 Pesos
3-Orquidia:Planta parasitaria muy bella, sobrevive de otras plantas                                      -3000 pesos
4-Copihue:Tradicional de la region:                                                                      -10.000 Pesos
5-Rosas rojas:Excelente opicion para el dia de los enamorados                                            -7000 Pesos"""

"""genera un archivo txt que almacene tus primeras 5 plantas en tu inventario y que quede abierto para almacenar infinitamente
"""

with open ("daos.txt", "w") as archivo:
    archivo.write(A)
