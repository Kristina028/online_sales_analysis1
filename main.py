from product_manager import ProductManager
from cart import Cart

def main():
    manager = ProductManager()
    cart = Cart()

    manager.add_product(1, "Laptop", 999.99)
    manager.add_product(2, "Phone", 499.99)
    manager.add_product(3, "Tablet", 299.99)

    print("Available Products:")
    for info in manager.list_products():
        print(info)

    product_id = int(input("Enter product ID to add to cart: "))
    product = manager.get_product_by_id(product_id)
    cart.add_to_cart(product)

    print("\nYour Cart:")
    for item in cart.view_cart():
        print(item)

if __name__ == "__main__":
    main()
