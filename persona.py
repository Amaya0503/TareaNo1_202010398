class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def presentarse(self):
        return f"Hola, soy {self.name} y tengo {self.age} años."
