# Classe de base pour tous les animaux
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self):
        raise NotImplementedError("Cette méthode doit être implémentée dans une sous-classe.")

    def __str__(self):
        return f"{self.name} (Animal)"


# Classe pour le lion
class Lion(Animal):
    def speak(self):
        return f"{self.name} dit : Roar!"


# Classe pour le perroquet
class Parrot(Animal):
    def speak(self):
        return f"{self.name} dit : Squawk!"


# Classe pour le serpent
class Snake(Animal):
    def speak(self):
        return f"{self.name} dit : Sssss!"


# Classe pour le chien
class Dog(Animal):
    def speak(self):
        return f"{self.name} dit : Woof!"


# Gestionnaire du zoo
class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal: Animal):
        self.animals.append(animal)

    def make_all_animals_speak(self):
        return [animal.speak() for animal in self.animals]

    def list_animals(self):
        return [str(animal) for animal in self.animals]


# Exemple d'utilisation
# Création des animaux
lion = Lion("Simba")
parrot = Parrot("Polly")
snake = Snake("Kaa")
dog = Dog("Rex")

# Création du zoo
my_zoo = Zoo()
my_zoo.add_animal(lion)
my_zoo.add_animal(parrot)
my_zoo.add_animal(snake)
my_zoo.add_animal(dog)

# Liste des animaux dans le zoo
print("Liste des animaux dans le zoo :")
for animal in my_zoo.list_animals():
    print(animal)

# Faire parler tous les animaux
print("\nLes animaux parlent :")
for sound in my_zoo.make_all_animals_speak():
    print(sound)
