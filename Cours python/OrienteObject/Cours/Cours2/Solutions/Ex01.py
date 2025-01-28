class Animal:
    def speak(self):
        return "I am an animal."


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


# Exemple d'utilisation
dog = Dog()
cat = Cat()

print(dog.speak())  # Woof!
print(cat.speak())  # Meow!
