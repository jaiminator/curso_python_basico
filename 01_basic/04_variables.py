# Declaración y asignación de variables
name = "Pepe"
edad = 34

# Imprimir variables
print("Nombre:", name)
# Reasignar variables
name = "Jaime"
print(name)
print(edad)

# OJO! No puedes utilizar palabras reservadas como nombres de variables
# class = "Hola" # dará error

# Tampoco en los siguientes casos:
# 1. Nombres de variables que empiecen con un número
# ejemplo: 3name = "Pedro"

# 2. Nombres de variables que contengan espacios
# ejemplo: nombre persona = "Pedro"

# 3. Nombres de variables que contengan caracteres especiales (excepto el guion bajo "_")
# ejemplo: nombre-persona = "Pedro"

# OTRO APUNTE IMPORTANTE: En Python, no hay variables constantes, pero por convención,
# se utilizan nombres en mayúsculas para indicar que una variable no debe cambiar su valor.