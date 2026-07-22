###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

print("\nEJERCICIO 1")

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
if (num1 > num2):
    print(num1, "es mayor que", num2)
elif (num1 < num2):
    print(num2, "es mayor que", num1)
else:
    print("Los dos números son iguales")


# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

print("\nEJERCICIO 2")
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
operacion = input("Qué operación quiere realizar?: (OPCIONES: 'suma','resta', multiplica' o 'divide'): ")

if operacion == 'suma':
    print(f"La suma da:", numero1 + numero2)
elif operacion == 'resta':
    print(f"La resta da:", numero1 - numero2)
elif operacion == 'multiplica':
    print(f"La multiplicción da:", numero1 * numero2)
elif operacion == 'divide':
    if numero2 == 0:
        print("Error! No puedes dividir entre 0")
    else:
        print(f"La división da:", numero1 / numero2)
else:
    print("Error! No has introducido bien la opción")


# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

print("\nEJERCICIO 3")
anio = int(input("Introduce un año: "))
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")


# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

print("\nEJERCICIO 4")
edad = int(input("Cuántos años tienes?: "))
if edad >= 0 and edad < 3:
    print("Eres un bebé")
elif edad >= 3 and edad < 13:
    print("Eres un niño")
elif edad >= 13 and edad < 18:
    print("Eres un adolescente")
elif edad >= 18 and edad < 65:
    print("Eres un adulto")
else:
    print("Eres una persona mayor")