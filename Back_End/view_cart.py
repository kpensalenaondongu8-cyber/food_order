from read_write_cart import load_cart
from read_write_cart import save_cart

import json

def View_Cart():

    # load data from cart
        item_cart = load_cart()

    # get each item in cart    
        for category_name, items_list in item_cart.items():
              print(f"\n---- {category_name.upper()} ----")
              print(f"{items_list}")
