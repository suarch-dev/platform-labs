###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

#print("Dame 2 números")
#num1 = input("primero:\n")
#num2 = input("segundo:\n")

#if num1 > num2:
#    print(num1, "es mayor que", num2)
#elif num1 == num2:
#    print(num1, "es el mismo número")
#else:
#    print(num1, "es menor que", num2)

#print("Hagamos una operación rápida")
#num1 = input("Dame un número:\n")
#n1 = int(num1)
#num2 = input("Ahora otro:\n")
#n2 = int(num2)
#operacion = input("Ahora una operación:\n")

#if operacion == "+":
#    print("Resultado:", n1 + n2)
#elif operacion == "-":
#    print("Resultado:", n1 - n2)
#elif operacion == "*":
#    print("Resultado:", n1 * n2)
#elif operacion == "/" and n2 != 0:
#    print("Resultado:", n1 / n2)
#elif operacion == "/" and n2 == 0:
#    print("No se puede dividir entre cero")

print("Adivinemos si es año bisiesto")
year = input("Dime un año\n")
año = int(year)
con1 = año % 4
con2 = año % 100
con3 = año % 400


if con1 == 0 and (con2 != 0 or con3 == 0):
    print("El año es bisiesto")
else:
    print("No lo es")

# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

age = input("Dame tu edad\n")
edad = int(age)

if edad <= 2:
    print("Eres un bebe")
elif edad <= 12:
    print("Eres un niño")
elif edad <= 17:
    print("Eres un adelescente")
elif edad <= 64:
    print("Eres un adulto")
else:
    print("Sos adulto mayor")
