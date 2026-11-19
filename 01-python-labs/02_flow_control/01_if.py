###
# 01 - Sentencias condicionales (if, elif, else)
# Permite ejecutar bloque de codigo solo si cumple las condiciones
###

#import subprocess
#subprocess.run("clear")

print("Sentencia simple condicional")

edad = 18
if edad >= 18:
    print("Eres mayor de edad")

edad = 15
if edad >= 18:
    print("Eres mayor de edad")

###

print("Sentencia condicional con else")

edad = 16
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

###

print("Sentencia condicional con elif")

nota = 3

if nota >= 9:
    print("!SObresaliente!")
elif nota >= 7:
    print("¡Notable!")
elif nota >= 5:
    print("Aprobado!")
else:
    print("¡no está calificado!")

print("Condiciones múltiples")
edad = 25
tiene_carnet = True

if edad >= 18 and tiene_carnet:
    print("Perfect")
else:
    print("infractor")

print("Anidar condiciones")

edad = 29
dinero = False

if edad < 18:
    print("No puedes entrar")
elif dinero:
    print("Puedes ir")
else:
    print("Quédate en casa")

number = 5
if number: # True
    print("El número no es cero")

number = 0
if number: # False
    print("Aquí no entra nunca")

nombre = ""
if nombre: #false
    print("El nombre no esta vacío")

numero = 3 #asignacion
es_el_tres = numero == 3 #comparacion
if es_el_tres:
    print("El nñumero es 3")

print("La condición Ternaria:")
#forma concisa de un "if-else"
#[código si cumple la condición] if [condición] else [código que no cumple]

edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)

