"""
Los dueños del vivero "Jan Joaquín", necesian realizar un programa en python, y para ello
cuentan con su nulo talento como desarolladores.
El programa debe ayudar con el inventario y venta de plantas.

A continuación los diez productos más vendidos;
"""
A="""
1.Rosas Blancas (Excelente para esta primavera)__________$2000
2.Mata de navidad (Traída de Mexico)_____________________$5000
3.Orquídea (Planta parasitaria muy bella)________________$3000
4.Copihue (Planta originaria de la Región)_______________$10000
5.Rosas Rojas (Excelente eleccion para ponerla)__________$7000
"""
"""
Genera un archivo TXT que almacene las primeras cinco plantas, y quede disponible para
almacenar datos infinitamente.
"""
with open ("plantas.txt", "w", encoding="utf-8") as archivo:
    archivo.write(A)
