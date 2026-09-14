from increase_cart import increase_quantity
from decrease_cart import decrease_quantity

from increase_cart import increase_quantity
from decrease_cart import decrease_quantity

def modify_cart(item, action, amount=1):
  
    if action == "increase":
        increase_quantity(item, amount)
        
    elif action == "decrease":
        decrease_quantity(item, amount)
        
    else:
        print(f"Error: '{action}' is an invalid action.")
