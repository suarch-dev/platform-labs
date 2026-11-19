###
# 02 - Bucles (for)
# Permite ejecutar un bloque de codigo
# repetidamente mientras itera un iterable o una lista
###

import subprocess
subprocess.run("clear")

# Iterar una lista
frutas = ["manzana", "pera", "mandarina"]
for fruta in frutas:
  print(fruta)

# Iterar sobre cualquier cosa que sea iterable
string = "nuartek"
for caracter in string:
  print(caracter)

# enumerate()
frutas = ["manzana", "pera", "mandarina"]
for index, fruta in enumerate(frutas):
  print(f"el index es {index} y la fruta {fruta}")

# bucles anidados
letras = ["A", "B", "C"]
numeros = [1, 2, 3]

for letra in letras:
  for numero in numeros:
    print(f"{letra}{numero}")

# break
print("\nbreak:")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for idx, animal in enumerate(animales):
  print(animal)
  if animal == "loro":
    print(f"El loro está escondido en el índice {idx}")
    break

# continue
print("\ncontinue:")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for idx, animal in enumerate(animales):
  if animal == "loro": continue
  print(animal)

# Comprensión de listas
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
animales_mayus = [animall.upper() for animall in animales]
print(animales_mayus)

# Muestra numeros pares de una lista
pares = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
print(pares)