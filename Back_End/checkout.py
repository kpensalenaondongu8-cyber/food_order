from read_write_cart import load_cart, save_cart
from read_write_menu import load_menu, save_menu


def deduct_stock(cart):
    menu = load_menu()
    for category, dishes in menu["categories"].items():
        for dish in dishes:
            if dish["name"] in cart:
                purchased_qty = cart[dish["name"]]["quantity"]
                dish["quantity"] = max(0, dish["quantity"] - purchased_qty)
    save_menu(menu)


def checkout():
    cart = load_cart()
    if not cart:
        print("Your cart is empty! Add some delicious food first.")
        return

    total = 0
    print("\n--- RECEIPT ---")
    for food, details in cart.items():
        quantity = details["quantity"]
        price = details["price_per_unit"]

        sub_total = quantity * price
        total += sub_total

    print("----------------")
    print(f"Your Grand Total is: ${total:,.2f}")

    deduct_stock(cart)

    cart.clear()
    save_cart(cart)
    print("Checkout successful! Your cart has been reset.")
    return total