from profesor import Profesor
from estudiante import Estudiante
from secretaria import Secretaria

profesor = Profesor("Pablo", 22, "Física")
estudiante = Estudiante("Fatima", 20, "Universidad")
secretaria = Secretaria("Michelle", 20, "Jurídica")

print(profesor.presentarse())
print(profesor.enseniar())

print(estudiante.presentarse())
print(estudiante.estudiar())

print(secretaria.presentarse())
print(secretaria.organizar())
