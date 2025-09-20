"""
la funcion print() se utiliza para mostrar informacion en la consola
"""
print("Hola Mundo") # Esto imprime un mensaje en la consola
print(123) # Esto imprime un numero en la consola
print(3.14) # Esto imprime un numero decimal en la consola


"""
la funcion input() se utiliza para recibir informacion del usuario a traves de la consola

"""

nombre = input("Ingrese su nombre: ") # Esto muestra un mensaje en la consola y espera a que el usuario ingrese un valor
edad = input("Porfavor ingrese su edad: ") # El valor ingresado por el usuario siempre sera de tipo string

print("Hola ", nombre) # Esto imprime el valor ingresado por el usuario
print("Tu edad es: ", edad) # Esto imprime el valor ingresado por el usuario


"""
El parametro *objects de la funcion print() puede recibir multiples valores separados por comas y los imprimira en la consola 
separados por un espacio por defecto

"""
print("Hola", "Mundo") # Esto imprime dos valores separados por un espacio
print("La suma de 2 + 2 es:", 2 + 2) # Esto imprime un mensaje y el resultado de una operacion matematica


"""
El parametro sep de la funcion print() se utiliza para especificar el separador entre los valores que se imprimen en la consola
"""
print("Hola", "Mundo", sep=", ") # Esto imprime dos valores separados por una coma y un espacio
print("Python", "es", "genial", sep=" - ") # Esto imprime tres valores separados por un guion y un espacio


