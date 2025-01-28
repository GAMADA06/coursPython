class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} €"


class OnlineStore:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def view_products(self):
        if not self.products:
            return "Aucun produit disponible."
        return "\n".join([str(product) for product in self.products])

    def sort_products_by_price(self):
        self.products.sort(key=lambda product: product.price)


# Exemple d'utilisation
store = OnlineStore()
store.add_product(Product("Laptop", 1200))
store.add_product(Product("Mouse", 25))
store.add_product(Product("Keyboard", 50))

print("Produits disponibles :")
print(store.view_products())

store.sort_products_by_price()
print("\nProduits triés par prix :")
print(store.view_products())
