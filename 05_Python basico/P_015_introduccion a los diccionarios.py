# Crear un diccionario literal
persona = {
    "nombre": "Leonel",
    "edad": 20,
    "estudiante": True
}
print("Diccionario inicial:", persona)

# Acceder a valores por su clave
print("Nombre:", persona["nombre"])  # imprime "Leonel"
print("Edad:", persona.get("edad"))  # imprime 20

# Modificar un valor existente
persona["edad"] = 21
print("Diccionario después de modificar edad:", persona)

# Agregar una nueva clave-valor
persona["ciudad"] = "Guadalajara"
print("Después de agregar ciudad:", persona)

# Eliminar un elemento
del persona["estudiante"]
print("Después de eliminar 'estudiante':", persona)

# Recorrer el diccionario
print("Recorriendo claves y valores:")
for clave, valor in persona.items():
    print("-", clave, ":", valor)

# Ver solo las claves o los valores
print("Claves:", persona.keys())
print("Valores:", persona.values())
