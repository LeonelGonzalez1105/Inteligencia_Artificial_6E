
# --- Mutabilidad e Inmutabilidad ---
lista = [1, 2, 3]         # lista mutable
lista[0] = 99             # se puede cambiar
print("Lista mutable modificada:", lista)

tupla = (1, 2, 3)         # tupla inmutable
# tupla[0] = 99           
print("Tupla inmutable:", tupla)

cadena = "Hola"
# cadena[0] = "M"         #error: no se puede modificar un string
print("Cadena inmutable:", cadena)

# --- Hashabilidad ---
print("Hash de un número:", hash(10))              # los números son hashables
print("Hash de una cadena:", hash("Leonel"))       # las cadenas también
print("Hash de una tupla:", hash((1, 2, 3)))       # tupla inmutable hashable

# Las listas NO son hashables (esto genera error):
# print(hash([1,2,3])) 

# Usando hashables como claves de un diccionario:
mi_dic = {
    "clave": "valor",
    (1, 2): "tupla como clave"
}
print("Diccionario con tupla como clave:", mi_dic)

# --- Iterabilidad ---
print("Recorriendo una lista (iterable):")
for elemento in lista:
    print("-", elemento)

print("Recorriendo una cadena (iterable):")
for letra in cadena:
    print("-", letra)

print("Recorriendo un diccionario (iterable por claves):")
for clave in mi_dic:
    print("-", clave, ":", mi_dic[clave])
