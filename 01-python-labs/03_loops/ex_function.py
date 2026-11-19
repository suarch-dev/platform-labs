###
# EJERCICIOS (for)
###

import subprocess
subprocess.run("clear")

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6:")

def tabla(a, b = range(1, 11)):
    for num in b:
        print(f"{a} x {num} = {a * num}")
    

print(tabla (3))
print(tabla(85))