class Student:
    def __init__(self, name: str, grades: list):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0


# Exemple d'utilisation
student1 = Student("Alice", [85, 90, 78])
student2 = Student("Bob", [60, 70, 80])

print(f"Moyenne d'Alice : {student1.average():.2f}")  # Moyenne d'Alice : 84.33
print(f"Moyenne de Bob : {student2.average():.2f}")  # Moyenne de Bob : 70.00
