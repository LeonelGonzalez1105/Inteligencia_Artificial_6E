
# Crear una lista de números
numeros = [10, 20, 30, 40, 50]  # lista literal

# Crear una lista de cadenas
frutas = ["manzana", "banana", "cereza"]

# Una lista puede tener elementos de distintos tipos
mixta = [1, "texto", True, 3.14]

# Acceder a elementos de la lista usando índices
print("Primer número:", numeros[0])   # primer elemento (índice 0)
print("Segunda fruta:", frutas[1])    # segundo elemento (índice 1)

# Modificar un elemento de la lista (mutabilidad)
numeros[2] = 35   # cambia el valor en índice 2 de 30 a 35
print("Lista de números modificada:", numeros)

# Métodos principales
frutas.append("naranja")    # agrega "naranja" al final
print("Frutas después de append:", frutas)

frutas.insert(1, "kiwi")    # inserta "kiwi" en la posición 1
print("Frutas después de insert:", frutas)

frutas.remove("banana")     # elimina "banana" de la lista
print("Frutas después de remove:", frutas)

ultimo = frutas.pop()       # elimina y devuelve el último elemento
print("Se eliminó:", ultimo)
print("Frutas después de pop:", frutas)

# Ordenar una lista de números
numeros.sort()              # ordena de menor a mayor
print("Lista de números ordenada:", numeros)

# Invertir una lista
numeros.reverse()           # invierte el orden
print("Lista de números invertida:", numeros)

# Longitud de la lista
print("Cantidad de frutas:", len(frutas))

# Recorrer la lista con un bucle for
print("Recorriendo lista de frutas:")
for fruta in frutas:
    print("-", fruta)
