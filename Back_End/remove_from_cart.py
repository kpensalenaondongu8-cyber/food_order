from read_write_cart import load_cart
from read_write_cart import save_cart
import json

def Rem_Fro_Cart(item):
        
        # open and load current data in cart
            data = load_cart()

        # update cart    
            if item in data:
                del data[item]
                print(f"{item} successfully deleted") 

        # Save the updated cart back to file
                save_cart(data)  
            else:
                print(f"{item} not in cart")

        