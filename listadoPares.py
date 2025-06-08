print("Bienvenido al listado de números pares.")

pares = list(range(2, 51, 2))

print("El listado de pares es el siguiente: ")

for i in range(len(pares)):
    if i == len(pares) - 1:
        print(pares[i])
    else:
        print(f"{pares[i]}", end=", ")