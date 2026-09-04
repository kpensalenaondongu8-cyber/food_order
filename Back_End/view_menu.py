from read_write_menu import load_menu
from read_write_menu import save_menu

import json

def display_Menu():


        data = load_menu()
        
        categories = data["categories"]
        
        for category_name, items_list in categories.items():
            print(f"\n--- {category_name.upper()} ---")
            
            for item in items_list:
                name = item["name"]
                price = item["price"]
                print(f"{name}: ${price:.2f}")