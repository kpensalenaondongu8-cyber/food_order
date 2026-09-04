from read_write_cart import load_cart
from read_write_cart import save_cart
import json

def Rem_Fro_Cart(item):
        
            data = load_cart()

            if item in data:
                del data[item]
                print(f"{item} successfully deleted") 

                save_cart(data)  
            else:
                print(f"{item} not in cart")

        