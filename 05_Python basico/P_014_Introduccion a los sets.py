
# Crear un set literal
frutas = {"manzana", "banana", "cereza"}
print("Set original:", frutas)

# Los sets eliminan duplicados automáticamente
numeros = {1, 2, 2, 3, 3, 4}
print("Set sin duplicados:", numeros)

# Agregar elementos
frutas.add("naranja")
print("Después de agregar naranja:", frutas)

# Eliminar elementos
frutas.remove("banana")  # elimina banana
print("Después de eliminar banana:", frutas)

frutas.discard("pera")   # intenta eliminar pera (no existe, no da error)
print("Después de descartar pera (no existe):", frutas)

# Vaciar un set
# frutas.clear()
# print("Set vacío:", frutas)

# Operaciones de conjuntos
A = {1, 2, 3}
B = {3, 4, 5}

union = A | B              # unión
print("Unión A y B:", union)

interseccion = A & B       # intersección
print("Intersección A y B:", interseccion)

diferencia = A - B         # diferencia
print("Diferencia A - B:", diferencia)

# Recorrer un set con for (es iterable)
print("Recorriendo set de frutas:")
for fruta in frutas:
    print("-", fruta)


