import json

def Add_to_Cart(item_name, quantity):
    try:
        with open("cart.json", "r") as file:
            if file == "":
                cart = {}
            else:
                cart = json.load(file)
    except FileNotFoundError:
        cart = {}

    try:
        with open("menu.json", "r") as file:
            menu = json.load(file)
    except FileNotFoundError:
        print("Error: menu.json not found!")
        return

    if item_name not in menu:
        print("That item is not on the menu!")
        return
        
    available_stock = menu[item_name][0]
    price = menu[item_name][1]

    if quantity > available_stock:
        print(f" Not enough stock! Only {available_stock} left.")
        return

    if item_name in cart:
        cart[item_name][0] += quantity

    else:
     
        cart[item_name] = [quantity, price]

    with open("cart.json", "w") as file:
        json.dump(cart, file, indent=4)

    print(f"Added {quantity}x {item_name} to your cart successfully!")