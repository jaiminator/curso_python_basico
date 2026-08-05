import os
os.system("clear")

print("\n range():")
nums = range(10) # NO CREA UNA LISTA
listaNumeros = [num for num in nums] # Utilizando la comprensión de listas
print(nums)
print(listaNumeros)

#Generando una secuencia de números del 0 al 9
for num in range(10):
    print(num)

#range(inicio, fin)
for num in range(5, 10):
    print(num)

#range(inicio, fin, paso)
for num in range(0, 10, 2):
    print(num)

nums = range(10)
list_of_nums = list(nums) # Conversión de tipo 'range' a 'list'
print(list_of_nums)