class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Erreur : division par zéro"
        return a / b


# Exemple d'utilisation
calc = Calculator()
print(calc.add(3, 4))         # 7
print(calc.subtract(10, 3))   # 7
print(calc.multiply(5, 6))    # 30
print(calc.divide(8, 2))      # 4.0
