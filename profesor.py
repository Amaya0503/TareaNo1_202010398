from persona import Persona

class Profesor(Persona):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def enseniar(self):
        return f"Soy el profesor {self.name} y enseño {self.course}."
