from product import Product

class ProductManager:
    """Manages a collection of Product instances."""

    def __init__(self):
        self.products = []

    def add_product(self, product_id: int, name: str, price: float):
        product = Product(product_id, name, price)
        self.products.append(product)

    def get_product_by_id(self, product_id: int):
        for p in self.products:
            if p.id == product_id:
                return p
        return None

    def list_products(self):
        return [p.display_info() for p in self.products]
