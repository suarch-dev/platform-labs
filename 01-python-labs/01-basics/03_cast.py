###
# 03 - casting de types
# transformar un tipo de valor a otro
###

print("Conversion de tipos")
print(type(int("100")))

print(int("100") + 2)

print("100" + str(2))
###el resultado el 1002 porque concadena 100 + sin espacio + 2 en texto.###

print(int(3.1416))
print(int(3.51))
print(int(3.99))

#solo quita los decimales, no redondea

print(bool(3))
print(bool(0))
print(bool(-1))

### solo el "0" se transforma en FALSE###

print(bool(""))
print(bool(" "))
print(bool("False"))

#Solo detecta como False si no hay datos

print(round(2.5))
print(round(3.5))
print(round(2.51))
#redondea al PAR mas cercano