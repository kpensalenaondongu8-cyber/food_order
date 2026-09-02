def modify_quantity (item, new_quantity):

    if new_quantity <= 0:
        print("Quantity most not be less than or zero")

    elif item in cart:
        cart[item]["quantity"] = new_quantity
        print("Quantity Updated succesfully")

    else:
        print(f"{item} not in cart so cant't be modified")
        

modify_quantity("Mango", 8)