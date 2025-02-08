from persona import Persona

class Secretaria(Persona):
    def __init__(self, name, age, area):
        super().__init__(name, age)
        self.area = area

    def organizar(self):
        return f"Soy {self.name} y trabajo firmando contratos en la area de {self.area}."
