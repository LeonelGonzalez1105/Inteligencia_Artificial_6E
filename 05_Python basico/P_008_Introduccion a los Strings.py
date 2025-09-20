"""
la concatenacion de strings se realiza utilizando el operador + para unir dos o mas cadenas de texto en una sola cadena.
sirve para combinar informacion de diferentes fuentes en un solo mensaje o texto.
"""

# Ejemplo de concatenacion de strings
nombre = "Juan"
apellido = "Perez"
nombre_completo = nombre + " " + apellido # Se utiliza el operador + para unir las cadenas de texto
print("Nombre completo:", nombre_completo) # Esto imprime "Nombre completo: Juan Perez"


"""
fstings o formatted strings son una forma de incluir variables y expresiones dentro de cadenas de texto de manera sencilla y legible.
se crean colocando una f o F antes de las comillas de la cadena de texto y utilizando
llaves {} para incluir las variables o expresiones que se desean insertar en la cadena.

"""
# Ejemplo de fstrings
nombre = "Maria"
edad = 30
mensaje = f"Hola, mi nombre es {nombre} y tengo {edad} años." # Se utiliza f antes de las comillas y {} para incluir variables
print(mensaje) # Esto imprime "Hola, mi nombre es Maria y tengo 30 años
