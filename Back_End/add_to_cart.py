from read_write_cart import load_cart, save_cart

def add_to_cart(item, quantity):
    # 1. Load the active cart file
    cart = load_cart()
    
    # Standardize item casing (matches our .title() change)
    item = item.strip().title()

    # 2. Check if it already exists, or initialize it
    if item not in cart:
        # Default price assigned when a brand new item enters the cart
        cart[item] = {"quantity": 0, "price_per_unit": 5.99} 
    
    # 3. Add the user's requested quantity
    cart[item]["quantity"] += quantity
    print(f"Success: Added {quantity}x {item}(s) to your cart.")
    
    # 4. CRUCIAL FIX: Write the updated cart state back to cart.json!
    save_cart(cart)
