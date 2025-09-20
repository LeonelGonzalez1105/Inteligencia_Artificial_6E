
# Crear una tupla de números
numeros = (10, 20, 30, 40)

# Crear una tupla con diferentes tipos de datos
mixta = ("Hola", 3.14, True)

# Una tupla con un solo elemento necesita una coma final
un_elemento = (5,)  # ojo con la coma

# Acceder a elementos por índice
print("Primer número:", numeros[0])
print("Segundo elemento de mixta:", mixta[1])

# Métodos principales
repetidos = (1, 2, 2, 3, 2)
print("Cantidad de veces que aparece 2:", repetidos.count(2))
print("Índice de la primera aparición de 3:", repetidos.index(3))

# Recorrer tupla con un for
print("Recorriendo tupla de números:")
for n in numeros:
    print("-", n)

# Errores comunes con tuplas:
# numeros[0] = 99  # Esto genera error porque las tuplas son inmutables

# Si necesitas modificarla, conviértela en lista:
lista_temporal = list(numeros)
lista_temporal[0] = 99  # ahora sí se puede
print("Lista temporal modificada:", lista_temporal)

# Luego puedes volver a tupla si quieres
nueva_tupla = tuple(lista_temporal)
print("Nueva tupla a partir de la lista:", nueva_tupla)
