texto = "hola mundo"
vocales = "aeiou"
conteo: dict[str, int] = {} # Diccionario vacío

for letra in texto: # Recorremos letra por letra
    if letra in vocales: # Si la letra está en la lista de vocales...
        if letra in conteo: # Si ya la habíamos visto antes...
            conteo[letra] = conteo[letra] + 1 # Le sumamos 1
        else: # Si es la primera vez que la vemos...
            conteo[letra] = 1 # La creamos con valor 1

print(conteo)
# Resultado: {'o': 2, 'a': 1, 'u': 1}

print("\nEJERCICIO: Contador de frutas")
# 
# 1. Tienes la siguiente lista de frutas:
frutas = ["manzana", "platano", "manzana", "pera", "platano", "manzana"]

# 2. Crea un diccionario vacío llamado 'conteo'.
#
# 3. Recorre la lista de frutas con un bucle 'for'.
#
# 4. Dentro del bucle, comprueba si la fruta ya está en el diccionario:
#    - Si ya está, súmale 1 a su valor actual.
#    - Si no está, añádela al diccionario con un valor de 1.
#
# 5. Al terminar el bucle, imprime el diccionario 'conteo'.
#    El resultado esperado en la terminal debe ser exactamente:
#    {'manzana': 3, 'platano': 2, 'pera': 1}

conteo: dict[str, int] = {}

for fruta in frutas:
    if fruta in conteo:
        conteo[fruta] += 1
    else:
        conteo[fruta] = 1

print(conteo)