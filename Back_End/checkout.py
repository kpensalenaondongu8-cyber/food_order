def checkout(cart):

    total = 0

    for food, details in cart.items():

      quantity = details["quantity"]
      price = details["price"]

      sub_total = quantity*price
      total += sub_total

    print(f"Your total is ₦{total}")    

checkout()