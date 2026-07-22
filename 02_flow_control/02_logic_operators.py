# Importamos 'os' para limpiar la consola antes de ejecutar el archivo Python
import os
os.system("clear")

# Operadores lógicos (and, or, not)

print("\n Condiciones múltiples")
edad = 25
tiene_carnet = False

if edad >= 18 and tiene_carnet:
    print("Puedes conducir")
else:
    print("Policia!")

es_fin_de_semana = False
if not es_fin_de_semana:
    print("Oye, que es fin de semana!")

print("\n Anidar condiciones")
edad = 16
tiene_dinero = True
if edad >= 18:
    if tiene_dinero:
        print("Puedes entrar a la discoteca")
    else:
        print("Quédate en la casa")
else:
    print("No puedes entrar a la discoteca")

if edad < 18:
    print("No puedes entrar a la discoteca")
elif tiene_dinero:
    print("Puedes entrar a la discoteca")
else:
    print("Quédate en la casa")