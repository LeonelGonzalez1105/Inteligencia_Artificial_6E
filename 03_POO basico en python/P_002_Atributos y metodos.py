# Definimos una clase Animal
class Animal:
    def __init__(self, nombre, especie):
        # Estos son atributos: características del objeto
        self.nombre = nombre
        self.especie = especie

    # Este es un método: acción que puede hacer el objeto
    def presentar(self):
        print(f"Hola, soy {self.nombre} y soy un {self.especie}.")

    # Otro método: otra acción
    def hacer_sonido(self, sonido):
        print(f"{self.nombre} hace: {sonido}")

# Creamos objetos (instancias) de la clase Animal
animal1 = Animal("Firulais", "perro")
animal2 = Animal("Michi", "gato")

# Usamos sus métodos
animal1.presentar()          # Usa atributos para presentarse
animal1.hacer_sonido("guau") # Ejecuta acción específica

animal2.presentar()
animal2.hacer_sonido("miau")

# Podemos cambiar atributos (son mutables)
animal1.nombre = "Rex"
animal1.presentar()  # ahora se presenta con su nuevo nombre
