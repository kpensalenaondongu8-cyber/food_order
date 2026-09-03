from read_write_cart import load_cart, save_cart

def checkout():
    # 1. Load the live cart database
    cart = load_cart()
    
    # Safety Check: If the cart is empty, stop early
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
    
    # 2. Clear the cart data out completely upon successful checkout
    cart.clear()
    save_cart(cart)
    print("Checkout successful! Your cart has been reset.")
    
    # Return the total so your main loop can use it for payment processing
    return total
