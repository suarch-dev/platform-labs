###
# 05 - Entrada de usuario
# versión simplificada
#Permite obtener datos del user a través de console
###

print("Hola, quién eres?")
name = input()

print(f"Hey {name}, enchanté")

#otra forma

name = input("Hey, who r u?")
print(f"Hey {name}, enchanté")
#diferencia: la respuesta queda a la altura de la pregunta

name = input("Hey, who r u?\n")
#se añade salto de linea

#age = input("Qué edad tenes?\n")
#print(f"Dentro de 10 años tendrás {age + 10}")
#da error porque el input es una cade de texto

#FORMA CORRECTA
age = input("Qué edad tenes?\n")
age = int(age)
print(f"Dentro de 10 años tendrás {age + 10}")

#MULTIPES VALORES A LA VEZ
country, city = input("En qué país y ciudad\n").split()
print(f"Vives en {country}, {city}")