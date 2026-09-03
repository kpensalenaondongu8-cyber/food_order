from read_write_cart import load_cart, save_cart

def increase_quantity(item, amount=1):
    cart = load_cart()
    
    if item not in cart:
        print(f"{item} not in cart")
       
    cart[item]["quantity"] += amount
    print(f"You added {amount} {item}(s).")   
    
    save_cart(cart)
