from read_write_cart import load_cart, save_cart

def increase_quantity(item, amount=1):
    cart = load_cart()
    
    if item not in cart:
        cart[item] = {"quantity": 0, "price_per_unit": {price_per_unit}} 
       
    cart[item]["quantity"] += amount
    print(f"Success: Added {amount} {item}(s).")   
    
    save_cart(cart)
