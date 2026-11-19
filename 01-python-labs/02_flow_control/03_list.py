###
# 03 - Listas
# Secuencias mutables de elementos
# Pueden contener  elementos de diferentes tipos.
###

import os
os.system("clear")

# Creaciçon de listas
print("Crear listas") 
list1 = [1, 2, 3, 4, 5]
list2 = ["manzanas", "peras", "plátanos"]
list3: list[int | str | bool] = [1, "peras", True]

list_vide = []
list_of_lists = [[1, 2], [3, 4], ["bingo", 6]]
matrix = [[3, 2], [5, 4]]

print(list1)
print(list2)
print(list3)
print(list_vide)
print(list_of_lists)
print(matrix)

# Acceso a elementos por índice
print("Acceso a elementos") #el cero cuenta
print(list2[0]) #el primero
print(list2[-1]) #el último
print(list_of_lists[2][0])

# Slicing de listas

print(list1[1:4])
#la posición 1 la incorpora
#pero la pos.2 es el limite, no entra
print(list1[1:4]) # [2, 3, 4]
print(list1[:3]) # [1, 2, 3]
print(list1[3:]) # [4, 5]
print(list1[:]) # [1, 2, 3, 4, 5]

# El tercer parámetro es el paso (step)
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(list1[::2]) # para devolver índices pares
print(list1[::-1]) # para devolver índices inversos

# Modificar una lista
list1[0] = 20
print(list1)

# Añadir elementos a una lista
lista1 = [1, 2, 3]

# forma larga y menos eficiente
lista1 = lista1 + [4, 5, 6]
print(lista1)

# forma corta y más eficiente
lista1 += [7, 8, 9]
print(lista1)

# Recuperar longitud de una lista
print("Longitud de la lista:", len(lista1))