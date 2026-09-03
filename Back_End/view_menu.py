from read_write_menu import load_menu
from read_write_menu import save_menu

import json

def display_Menu():

#    open and load data  from menu

        data = load_menu()
        
        # Get the categories dictionary
        categories = data["categories"]
        
        # Loop through each category name 
        for category_name, items_list in categories.items():
            print(f"\n--- {category_name.upper()} ---")
            
            # Loop through each item dictionary inside that category list
            for item in items_list:
                name = item["name"]
                price = item["price"]
                print(f"{name}: ${price:.2f}")