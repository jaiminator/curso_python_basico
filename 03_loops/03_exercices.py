import os
os.system("clear")

###
# EJERCICIOS (range)
###

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1:")
numeros = range(1, 11)
for num in numeros:
    print(num)

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2:")
impares = range(1, 21, 2)
for impar in impares:
    print(impar)

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3:")
multiplos5 = range(5, 51, 5)
for multiplo5 in multiplos5:
    print(multiplo5)

# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4:")
numeros = range(10, 0, -1)
for num in numeros:
    print(num)

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5:")
numeros = range(1, 101)
suma = 0
for num in numeros:
    suma += num
print(f"La suma total es: {suma}")

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6:")
numero = int(input("Introduce un número: "))
print(f"\nLA TABLA DEL {numero}")
tablaMultiplicar = range(1, 11)
for multiplicador in tablaMultiplicar:
    print(f"{numero} x {multiplicador} = {multiplicador * numero}")