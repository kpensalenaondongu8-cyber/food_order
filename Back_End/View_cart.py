def view_cart(cart):

    if len(cart) == 0:
        print("Your cart is empty") 

    for food, details in cart.items():

        quantity = details["quantity"]
        price = details["price"]
        result = quantity * price

        print(f"food: {food}, quantity: {quantity}, price: ₦{price}, subtotal: ₦{result}")