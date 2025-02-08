from persona import Persona

class Estudiante(Persona):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def estudiar(self):
        return f"Soy {self.name} y estoy estudiando en el grado {self.grade}."
