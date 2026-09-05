from read_write_cart import load_cart, save_cart
from read_write_menu import load_menu


def get_price(item):
    menu = load_menu()
    for category, dishes in menu["categories"].items():
        for dish in dishes:
            if dish["name"] == item:
                return dish["price"]
    return 0


def increase_quantity(item, amount=1):
    cart = load_cart()
    if item not in cart:
        cart[item] = {"quantity": 0, "price_per_unit": get_price(item)}
    cart[item]["quantity"] += amount
    print(f"Success: Added {amount} {item}(s).")
    save_cart(cart)