# 1: Crear una clase Student que tiene los siguientes atributos: name, age y grades (una lista de números)
# 2. Crear un constructor que inicialice los atributos
# 3. Crear un método llamado add_grade que recibe un número como parámetro y lo agrega a la lista grades.
# 4. Crear otro método llamado average_grade que calcule y retorne la nota promedio de la lista de notas grades

import random


class Student:
    def __init__(self):
        self.name = []
        self.age = [10, 15]
        self.grades = [6, 11]

    def add_grade(self):
        n = random.randint(6, 11)
        self.grades.append(n)

    def average_grade(self):
        pass



estudiante = Student()
print(estudiante.add_grade())
print(estudiante.grades)







