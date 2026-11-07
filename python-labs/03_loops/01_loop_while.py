###
# 01 - Bucles (while)
# Permite ejecutar un bloque de codigo
# repetidamente mientras se cumpla una condición
###

import subprocess
subprocess.run("clear")

print("Bucle con una simple condición")

contador = 0
while contador <= 5:
    print(contador)
    contador += 1 #importante para evitar bucle infinito

#while True:
#    print("Hola")
#BUCLE INFINITO
#DEBE HABER CONDICION DE SALIDA

# "break" para romper loop

#while True:
#    print("hola")
#    contador +=1
#    if contador == 5:
#        break #salir del loop

print("Bucle continue")
#Salta esa iteración en concreto
#continua el loop

contador = 0
while contador < 10:
    contador += 1
    if contador % 2 == 0:
        continue
    print(contador)

print("Bucle while con else")
contador = 0
while contador < 5:
    print(contador)
    contador += 1
else:
    print("Loop terminó")
# ELSE asegura que un loop termine

#ejemplo y TRY/Except

numero = -1
while numero < 0:
    try:
        numero = int(input("Escribe un numero positivo: "))
        if numero < 0:
            print("Debe ser positivo!!")
    except:
        print("Entrada no válida")
print(f"El numero introducido es {numero}")