# Definimos una clase (molde)
class Persona:
    # Método especial __init__ se ejecuta al crear un objeto
    def __init__(self, nombre, edad):
        self.nombre = nombre  # atributo nombre
        self.edad = edad      # atributo edad

    # Un método (comportamiento)
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear (instanciar) objetos a partir de la clase Persona
persona1 = Persona("Leonel", 20)
persona2 = Persona("Ana", 25)

# Usar sus métodos
persona1.saludar()
persona2.saludar()

# Cambiar atributos (porque son mutables)
persona1.edad = 21
persona1.saludar()
