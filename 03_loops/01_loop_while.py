import os
os.system("clear")
# Bucles (while)

# Bucle con una sola condición
print("\n Bucle while:")
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# utilizando break para romper el bucle
print("\n Bucle con break")
contador = 0
while True:
    print(contador)
    contador += 1
    if contador == 5:
        break # salir del bucle

print("\n Bucle con continue")
contador = 0
while contador < 10:
    contador += 1

    if contador % 2 == 0:
        continue

    print(contador)

print("\n Bucle while con else")
contador = 0
while contador < 5:
    print(contador)
    contador += 1
else:
    print("El bucle ha terminado")

# EJERCICIO DE EJEMPLO: pedirle al usuario un número que tiene
# que ser positivo si no, no le dejamos en paz
# Sentencia try/except caza un error y lo lanzamos para que no falle el programa
print("\n EJERCICIO DE EJEMPLO (tratado de error con try/except)")
numero = -1
while numero < 0:
  try:
    numero = int(input("Escribe un número positivo: "))
    if numero < 0:
      print("El número debe ser positivo. Intenta otra vez, majo o maja.")
  except:
    print("Lo que introduces debe ser un número, que si no peta!")

print(f"El número que has introducido es {numero}")