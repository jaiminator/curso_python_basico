# Sentencias condicionales if, elif y else

print("\n Sentencia simple condicional:")

edad = 19

if edad >= 18:
    print("Eres mayor de edad. Enhorabuena!")

edad = 16
if edad >= 18:
    print("Eres mayor de edad. Enhorabuena!")

print("\n Sentencia condicional con else:")

edad = 17

if edad >= 18:
    print("Eres mayor de edad. Enhorabuena!")
else:
    print("Eres menor de edad")

print("\n Sentencia condicional con elif:")
nota = 7

if nota >= 9:
    print("Excelente!")
elif nota >= 7:
    print("Notable!")
elif nota >= 5:
    print("Bien!")
else:
    print("Suspendido!")