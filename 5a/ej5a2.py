"""
Enunciado:
Implementa una jerarquía de clases para representar
animales que pueden emitir sonidos. Existe una clase abstracta "Animal"
que define un método abstracto "make_sound". También, implementa tres
clases concretas "Dog", "Cat" y "Duck" que heredan de la clase "Animal"
e implementan su propio método "make_sound" para representar el sonido
que cada animal emite.

Luego de implementar las clases debes crear una lista de animales
que incluya un perro, un gato y un pato, y se recorra la lista haciendo
que cada animal emita el sonido correspondiente usando la función
"make_sound" y se imprima el sonido que emite cada animal.

Clases:
    - Animal: Clase abstracta que representa la abstracción de un animal y
    define el método abstracto "make_sound".
    - Dog: Clase que hereda de "Animal" y representa un perro, define su
    propio método "make_sound" que devuelve "Woof".
    - Cat: Clase que hereda de "Animal" y representa un gato, define su
    propio método "make_sound" que devuelve "Meow"
    - Duck: Clase que hereda de "Animal" y representa un pato, define su
    propio método "make_sound" que devuelve "Quack"

Ejemplo:
    Entrada:
        animals = [Dog(), Cat(), Duck()]
        for animal in animals:
            print(f'{animal.make_sound()}')

    Salida:
        Woof
        Meow
        Quack

"""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof"

class Cat(Animal):
    def make_sound(self):
        return "Meow" 

class Duck(Animal):
    def make_sound(self):
        return "Quack"

# Create a list of animals here
animals = [Dog(), Cat(), Duck()]
# Print animals sounds
for animal in animals:
    print(animal.make_sound())
