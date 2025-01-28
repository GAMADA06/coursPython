class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Je m'appelle {self.name} et j'ai {self.age} ans."


# Exemple d'utilisation
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1.introduce())  # Je m'appelle Alice et j'ai 25 ans.
print(person2.introduce())  # Je m'appelle Bob et j'ai 30 ans.
