###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí

#name = input("hola, quien sos?\n")
#city = input("y de dónde?\n")

#print(f"Genial, eres {name}.\nY sos de {city}.")

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
print(int("12345"))
print(float(int("12345")))

print(int(float(3.99)))
print("Pierde los decimales, no redondea.")

cadena = 12345
cad_entero = int(cadena)
ent_float = float(cad_entero)

print("Number entero:", cad_entero)
print("Float en entero:", ent_float)

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí

#name = input("Nombre?\n")
#age = input("Edad?\n")
#height = input("Altura?\n")

#print(f"Genial, sos {name}, de {age} años de edad y {height}m de altura")

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

pi_variable = 3.1416

print(round(pi_variable))
print(int(pi_variable/2))