from read_write_cart import load_cart, save_cart

def add_to_cart(item, quantity):
    cart = load_cart()
    
    item = item.strip().title()

    if item not in cart:
        cart[item] = {"quantity": 0, "price_per_unit": 5.99} 
    
    cart[item]["quantity"] += quantity
    print(f"Success: Added {quantity}x {item}(s) to your cart.")
    
    save_cart(cart)
