###
# 04 - Listas Métodos
# Métodos para trabajar con listas
###

import os
os.system("clear")

lista1 = [1, 2, 3, 4, 5]

lista1.append(6) #add 1 elemento al final
print(lista1)

lista1.insert(1, "20") #inserta en la posicion
print(lista1)

lista1.extend(["@", "a"]) #add elementos al final
print(lista1)

lista1.remove("@") #elimina el primer elemento que corresponda
print(lista1)

ultimo = lista1.pop() #elimina el ultimo elemento y ademas lo devuelve
print(ultimo)
print(lista1)

#pop "(-1)" por defecto
#pop se pasa con indices

lista1.pop(2) #elimina el segundo elemento
print(lista1)

del lista1[-2]
print(lista1)
#elimina a lo bestia

lista1.clear() #ELIMINA TODOS LOS ELEMENTOS
print(lista1)

# Eliminar un rango de elementos
lista1 = ['🐼', '🐨', '🐶', '😿', '🐹']
del lista1[1:3] # eliminamos los elementos del índice 1 al 3 (no incluye el índice 3)
print(lista1)

# Más métodos útiles
print('Ordenar listas modificando la original')
numbers = [3, 10, 2, 8, 99, 101]
numbers.sort()
print(numbers)

print('Ordenar listas creando una nueva lista')
numbers = [3, 10, 2, 8, 99, 101]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

print("Ordenar una lista de cadenas de texto (todo minúscula)")
frutas = ['manzana', 'pera', 'limón', 'manzana', 'pera', 'limón']
sorted_frutas = sorted(frutas)
print(sorted_frutas)

print("Ordenar una lista de cadenas de texto (mezclas mayúscula y minúscula)")
frutas = ['manzana', 'Pera', 'Limón', 'manzana', 'pera', 'limón']
frutas.sort(key=str.lower)
print(frutas)

# Más cositas útiles
animals = ['🐶', '🐼', '🐨', '🐶']
print(len(animals)) # Tamaño de la listas -> 4
print(animals.count('🐶')) # Cuantas veces aparece el elemento '🐶' -> 2
print('🐼' in animals) # Comprueba si hay un '🐼' en la lista -> True
print('🐹' in animals) # -> False