Numeros=[5, 4, 2]

Numero_primo = 0
Numero_noprimo = 0

def es_primo(n):
    if n <= 1:
        return False
    for i in range (2, int(n/2)+1):
        if n% i == 0:
            return False
    return True

for i, numero in enumerate(Numeros):
    print(f"{i+1} número: {numero}",end="->")
    if es_primo(numero):
        print("Es primo")
        Numero_primo += 1
    else:
        print("No es primo")
        Numero_noprimo +=1

print("\nResultado")
print(f"Se ingresaron {Numero_primo} numero(s) primo")
print(f"Se ingresaron {Numero_noprimo} numero(s) no primo")
