from read_write_cart import load_cart, save_cart

def decrease_quantity(item, amount=1):
    cart = load_cart()
    
    # Optional: If the item isn't in the cart yet, initialize it
    if item not in cart:
        print(f"{item} not in cart") 
    else:   
        cart[item]["quantity"] -= amount
        print(f"You added {amount} {item}(s).")   
    
        if cart[item]["quantity"] <= 0:
            del cart[item]
            print(f"{item} have been temporary removed from your cart")
            
    save_cart(cart)
