###
# EJERCICIOS (for)
###

import subprocess
subprocess.run("clear")

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")

# numero = 2
# lista = []

# while numero <= 20:
#     lista.append(numero)
#     numero += 1
# print(lista)

# pares = [num for num in lista if num % 2 == 0]
# print(pares)

for numero in range(2, 21, 2): #range(inicio, fin, cada cuanto/paso)
    print(numero)

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")

numeros = [10, 20, 30, 40, 50]
media = 0
for num in numeros:
    media += num
print(media / len(numeros))

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")

numeros = [15, 5, 25, 10, 20]
max = 0

for compa in numeros:
    if compa > max:
        max = compa
print(max)

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")

palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# lista = []
# for cinco in palabras:
#     if len(cinco) > 5:
#         lista.append(cinco)
# print(lista)

lista_n = [cinco for cinco in palabras if len(cinco) > 5]
print(lista_n)

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")

palabras = ["casa", "arbol", "sol", "elefante", "eluna", "coche"]
filtro = str(input("Pon una letra: ")).lower()
contador = 0

for palabra in palabras:
    if palabra.lower().startswith(filtro):
        contador += 1

print(contador)