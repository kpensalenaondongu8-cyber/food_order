from read_write_cart import load_cart

def View_Cart():
    # 1. Load data from cart
    item_cart = load_cart()

    # 2. Check if the cart is completely empty
    if not item_cart:
        print("\n🛒 Your cart is empty.\n")
        return

    print("\n================ SHOPPING CART ================")
    grand_total = 0

    # 3. Loop through items correctly to fetch the keys and inner dictionaries
    for food_name, details in item_cart.items():
        quantity = details["quantity"]
        price_per_unit = details["price_per_unit"]
        
        # Calculate individual item subtotal
        item_subtotal = quantity * price_per_unit
        grand_total += item_subtotal
        
        # Print a cleanly spaced, readable line item
        print(f"• {food_name:<22} x{quantity:<3} (${price_per_unit:>6.2f} each) ---> ${item_subtotal:>6.2f}")

    print("===============================================")
    print(f"Total Cart Value: ${grand_total:.2f}\n")
