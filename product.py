class Product:
    """Represents a single product."""

    def __init__(self, product_id: int, name: str, price: float):
        self.id = int(product_id)
        self.name = name
        self.price = float(price)

    def display_info(self) -> str:
        return f"ID: {self.id} | Name: {self.name} | Price: {self.price:.2f}"

    def __repr__(self):
        return f"Product(id={self.id}, name={self.name!r}, price={self.price})"
