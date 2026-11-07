###
# EJERCICIOS (while)
###

import subprocess
subprocess.run("clear")

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")

numero = 10
while numero > 0:
    print(numero)
    numero -= 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")

numero = 1
suma = 0
while numero <= 20:
    if numero % 2 == 0:
        suma += numero
    numero += 1
print(suma)

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

#facto = 1
#try:
#    num = int(input("dame un numero positivo: "))
#     while num > 0:
#         facto *= num
#         num -= 1
#     print(f"El factorial es: {facto}")
# except:
#     print("entrada no valida") 

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

# password = "abc"
# while len(password) < 8:
#     password = input("introduce un pass: ")
#     if len(password) < 8:
#         print("debe tener al menos 8 carac")
# else:
#     print("contra valida")


# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

# multiplo = 1
# user = int(input("Te dare una tabla, dame un numero: "))
# while multiplo <= 10:
#     print(f"{user} x {multiplo} = {user * multiplo}")
#     multiplo += 1

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")

# ene = int(input("Introduce un numero: "))
# eme = ene
# while ene > 0:
#     if ene / (ene - 1) == 1:
#         print(ene)
#     ene -= 1

n = int(input("Introduce un número entero positivo N: "))
numero = 2
while numero <= n:
  es_primo = True  # Asumimos que el número es primo hasta que se demuestre lo contrario
  divisor = 2
  while divisor * divisor <= numero:  # Optimizamos: no es necesario probar divisores hasta numero
    if numero % divisor == 0:
      es_primo = False  # Si encontramos un divisor, no es primo
      break  # Salimos del bucle interior
    divisor += 1
  if es_primo:
    print(numero)
  numero += 1