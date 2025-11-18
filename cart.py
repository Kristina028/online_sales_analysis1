class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product):
        if product:
            self.items.append(product)
            print(f"Added to cart: {product.name}")
        else:
            print("Product not found!")

    def view_cart(self):
        if not self.items:
            return ["Cart is empty."]

        cart_list = []
        total = 0

        for item in self.items:
            cart_list.append(f"{item.name} - {item.price:.2f}")
            total += item.price

        cart_list.append(f"Total: {total:.2f}")
        return cart_list
