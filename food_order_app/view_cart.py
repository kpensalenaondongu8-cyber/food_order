from read_write_cart import load_cart

def View_Cart():
    item_cart = load_cart()

    if not item_cart:
        print("\n🛒 Your cart is empty.\n")
        return

    print("\n================ SHOPPING CART ================")
    grand_total = 0

    for food_name, details in item_cart.items():
        quantity = details["quantity"]
        price_per_unit = details["price_per_unit"]
        
        item_subtotal = quantity * price_per_unit
        grand_total += item_subtotal
        
        print(f"• {food_name:<22} x{quantity:<3} (${price_per_unit:>6.2f} each) ---> ${item_subtotal:>6.2f}")

    print("===============================================")
    print(f"Total Cart Value: ${grand_total:.2f}\n")
