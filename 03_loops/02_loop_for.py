import os
os.system("clear")

# Iterar una lista
print("\n Bucle for:")
ciudades = ["Valencia", "Alicante", "Castellón"]
for ciudad in ciudades:
    print(ciudad)

# Iterar sobre cualquier cosa que sea iterable
cadena = "metropolis"
for caracter in cadena:
    print(caracter)

# enumerate()
ciudades = ["Valencia", "Alicante", "Castellón"]
for index, value in enumerate(ciudades):
    print(f"El índice es {index} y su valor es: {value}")

# Bucles anidadas
letras = ["A", "B", "C"]
numeros = [1, 2, 3]
for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}")

# break
print("\nBreak")
animales = ["gato", "perro", "tortuga", "canario", "pez"]
for animal in animales:
    print(animal)
    if animal == "tortuga":
        break

# continue
print("\nContinue")
animales = ["gato", "perro", "tortuga", "canario", "pez"]
for animal in animales:
    if animal == "tortuga": continue
    print(animal)

#Compresión de listas
animales = ["gato", "perro", "tortuga", "canario", "pez"]
animales_mayus = [animal.upper() for animal in animales]
print(animales_mayus)

# Mostrar números pares de una lista
num_pares = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
print(num_pares)