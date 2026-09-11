from read_write_cart import load_cart, save_cart
from read_write_menu import load_menu, save_menu
from save_order import save_order

def deduct_stock(cart):
    menu = load_menu()
    for category, dishes in menu["categories"].items():
        for dish in dishes:
            if dish["name"] in cart:
                 purchased_qty = cart[dish["name"]]["quantity"]
                 dish["quantity"] = max(0, dish["quantity"] - purchased_qty)
    save_menu(menu)


def checkout(user_id):
    cart = load_cart()
    if not cart:
        print("Your cart is empty! Add some delicious food first.")
        return
    print("DEBUG -Cart contents right before checkout:", cart)
    total = 0
    for food, details in cart.items():
        quantity = details["quantity"]
        price = details["price_per_unit"]
        total += quantity * price

    save_order(user_id, cart)   

    deduct_stock(cart)
    cart.clear()
    save_cart(cart)
    return total