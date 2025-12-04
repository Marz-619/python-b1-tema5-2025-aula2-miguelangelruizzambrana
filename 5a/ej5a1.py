"""
Enunciado:
Crea una clase llamada "Student" con alta cohesión, que
almacene información básica de un estudiante (name, age y average)
y tenga dos métodos: "describe" y "grade". El método "describe"
debe devolver una cadena con la información básica del estudiante
y el método "grade" debe actualizar el promedio del estudiante con
una nueva calificación.

Parámetros:
    name = Una cadena que representa el name del estudiante.
    age = Un número entero que representa la edad del estudiante.
    average = Un número decimal que representa el promedio del estudiante.

Métodos:
    - describe() = Devuelve una cadena con la información básica del
    estudiante.
    - grade(new_grade) = Actualiza el promedio del estudiante con una
    nueva calificación.

Ejemplo:
    Entrada:
        student1 = Student("Juan", 20, 8.5)
        student1.grade(9.0)
        print(student1.describe())

    Salida:
        Name: Juan, Age: 20, Average: 8.75

"""

class Student:
    def __init__(self,name,age,average):
        self.name = name
        self.age = age
        self.average = average

    def describe (self):
        return f"Name: {self.name}, Age: {self.age}, Average: {self.average}"
    
    def grade (self,new_grade):
        self.average = (self.average + new_grade) / 2
    

       

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# student1 = Student("Pedro", 49, 8.5)
# print(student1.describe())
# student1.grade(9.2)
# print(student1.describe())
