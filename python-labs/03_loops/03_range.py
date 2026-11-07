###
# 03 - range()
# Permite crear secuencia de numeros
# ###

import subprocess
subprocess.run("clear")

nums = range(5) #NO CREA LISTA
print(nums)

for num in range(10):
    print(num)
#DA UNA SECUENCIA DE NUMEROS

print("saltos")
for num in range(2,10,3):
    print(num)

print("Countdown")
for num in range(10,0,-1):
    print(num)

#RANGE CREA NUMERO SOBRE LA MARCHA

nums = range(1,10)
list_of_nums = list(nums)
print(list_of_nums)

#REPETIR ALGO CON FOR Y RANGE
for _ in range(5):
    print("repetir")