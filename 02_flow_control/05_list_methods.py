import os
os.system("clear")

lista1 = ['a', 'b', 'c', 'd', 'e']

lista1.append('f') # Añade un elemento al final de la lista
print(lista1)

lista1.insert(2, '#') # Inserta un elemento en la posición que le indiquemos
print(lista1)

lista1.extend(['y', 'z']) # Añade varios elementos al final de la lista
print(lista1)

lista1.remove('#') # Elimina la primera aparición del valor en la lista
print(lista1)

lista1.pop(1) # Elimina el elemento del valor del índice asignado
print(lista1)

lista1.clear() # Elimina todos los elementos de la lista
print(lista1)

# Elimina un rango de elementos (slicing)
lista1 = [1, 2, 3, 4, 5]
del lista1[2:] # Elimina los elementos desde la posición '2' hasta el final
print(lista1)

# Ordenar listas
numeros = [2, 50, 34, 7, 6]
numeros.sort() # Ordena la lista de manera ascendente
letras = ['eclipse', 'casa', 'tierra', 'ocular']
letras.sort() # Ordena la lista de manera ascendente
print(numeros)
print(letras)

#Otros métodos
numeros = [1, 2, 3, 2, 4, 5, 1, 4, 2]
print(len(numeros)) # Longitud de la lista
print(numeros.count(2)) # Veces que aparece un elemento de la lista
print(4 in numeros) # Hay algún número 4 en la lista 'numeros' ? Sí