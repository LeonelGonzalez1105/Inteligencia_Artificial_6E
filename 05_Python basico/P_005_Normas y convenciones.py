"""
Existen algunas normas y convenciones a la hora de declarar variables en python

la primera regla es la sensibilidad a mayusculas y minusculas 
#nombre_variable
#NOMBRE_VARIABLE
#Nombre_Variable

"""

"""
Las varibales solo deben de utilizar letras, numeros y guiones bajos (_)

#nombre-variable (no es valido)
#nombre variable (no es valido)

"""
nombre_variable1 = 10
nombre_variable_1 = 10
nombre = 10



"""
No puedes comenzar una variable con un numero debe de ser con una letra o un guion bajo (_)
#1nombre (no es valido)
23nombre = 10 #no es valido

"""
_nombre = 10 #Esto esta correcto porque sigue regla pero no es recomendable
nombre2 = 10 #esto es valido

"""
no puedes utilizar palabras reservadas del lenguaje como nombres de variables
#for = 10 #no es valido

"""

for_var = 10 #esto es valido
var_for = 10 #esto es valido

"""
Una de las convenciuones es ser descriptivo con los nombres de las variables
fecha= hola #no es descriptivo
nombre= 7.32 #no es descriptivo
"""
fecha_nacimiento = "01/01/2000" #esto es descriptivo
precio_producto = 19.99 #esto es descriptivo
nombre_usuario = "juan123" #esto es descriptivo

"""
Otra convencion es utilizar el formato snake_case para los nombres de las variables
#nombreVariable (no es snake_case)
#NombreVariable (no es snake_case)
#nombre-variable (no es snake_case)

"""
nombre_variable = "juan" #esto es snake_case
nombre_completo = "juan perez" #esto es snake_case
precio_total = 100.50 #esto es snake_case
