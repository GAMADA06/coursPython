class Product:
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

    def buy(self, quantity: int):
        if quantity > self.stock:
            return "Quantité non disponible"
        self.stock -= quantity
        return f"Coût total : {self.price * quantity}"


# Exemple d'utilisation
product = Product("Laptop", 1200, 5)
print(product.buy(3))   # Coût total : 3600
print(product.buy(4))   # Quantité non disponible
