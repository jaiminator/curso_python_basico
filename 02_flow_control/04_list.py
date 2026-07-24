# Secuencias de elementos

print("\nCrear listas")
lista1 = [1, 2, 3, 4, 5]    #Lista de enteros
lista2 = ["Valencia", "Sevilla", "Badajoz"] #Lista de cadenas
lista3 = [1, "Manuel", True]    #Lista de tipos mixtos
lista_de_listas = [[1, 2], [4, 5]]
lista_vacia = []    #Lista vacía sin elementos

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)

# Acceder a elementos por índice
print("\nAcceso a elementos por índice")
print(lista2[0]) #Valencia
print(lista2[1]) #Sevilla
print(lista2[-1]) #Badajoz
print(lista2[-2]) #Sevilla

print(lista_de_listas[0][1]) #2

#Slicing (rebanado) de listas

lista_num = [1, 2, 3, 4, 5]
print(lista_num[1:4])
print(lista_num[:3])
print(lista_num[:])

#'Paso' añadido
lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista_num[::2]) #números impares de la lista
print(lista_num[1::2]) #números pares de la lista