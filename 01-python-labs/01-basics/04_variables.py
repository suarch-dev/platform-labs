###
# 04 - Variables
# guarda datos en memoria
# unico lenguaje de tipado dinámico y fuerte
###

#asignar una variable
my_name = "nuartek"
print(my_name)

age = 29
print(age)
#se puede reasignar el comando
age = 39
print(age)

#tipado dinámico: se determina en tiempo de ejecución

name = "nuartek"
print(type(name))

name = 29
print(type(name))

#tipadp fuerte: no realiza conversión automática

#print(10 + "2")
#da error, no convierte

print(f"Hola {my_name}, tengo {age - 10} años")
#f-string: literal de cadena de formato
#desde versión Python 3.6

#NO RECOMENDADO
name, age, city = "nuartek", 29, "Aqp"
print(name, age, city)

#Convenciones de nombres de variables
mi_nombre_de_variable = "ok"
#snake_case
nombre = "ok"

MiNombreDeVariable = "ko"
#PascalCase
minombredevariable = "ko"
#todojunto

mi_nombre_de_variable_123 = "ok"

MI_CONSTANTE = 3.14
#Python NO TIENE CONSTANTE
#UPPER CASE > constantes
#Se entiende que es un valor que NO deberia cambiar

#123123_variable = "ko"
#Var que inicia por número NO WORKS

#mi-variable = "ko"
#Guion para separar NOT WORKS

#mi variable = "ko"
#ESPACIO separar NOT WORK

#PALABRAS RESERVADAS
#False, None, True, and, as, assert, etc

nombre: int = "change"
#en Python no hay tipos, pero en el editor
#se puede activar
#el modo tipado estatico