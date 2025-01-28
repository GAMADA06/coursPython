class Student:
    def __init__(self, name: str):
        self.name = name


class School:
    def __init__(self):
        self.students = []

    def enroll(self, student: Student):
        self.students.append(student)

    def list_students(self):
        return [student.name for student in self.students]


# Exemple d'utilisation
school = School()
school.enroll(Student("Alice"))
school.enroll(Student("Bob"))

print(school.list_students())  # ['Alice', 'Bob']
