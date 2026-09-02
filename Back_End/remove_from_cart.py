
import json

def Remove_From_Cart (item):

   with open("cart.json", "r") as file:
      cart = json.load(file)

   if item in cart:
        del cart[item]   
        with open("cart.json", "w") as file:
                cart = json.dump(cart, file, indent=4)



        print(f"{item} deleted from cart succesfully")
   else:
        print(f"{item} Not in cart")
        