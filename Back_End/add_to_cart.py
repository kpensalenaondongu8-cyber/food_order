from read_write_menu import save_menu
from read_write_menu import load_menu
from read_write_cart import save_cart
from read_write_cart import load_cart
import json

def add_to_cart(item_name, quantity):
    # 1. Open and load the menu to see what items are available
    menu_data = load_menu()
    
    # Flatten all items from all categories into one easy-to-search list
    all_items = []
    for items_list in menu_data["categories"].values():
        all_items.extend(items_list)
        
    # Search for the requested item in the menu
    found_item = None
    for item in all_items:
        if item["name"].lower() == item_name.lower(): # Case-insensitive check
            found_item = item
            break
            
    # If the item doesn't exist or is out of stock, stop here
    if not found_item or not found_item["name"]:
        print(f"Error: '{item_name}' is currently unavailable.")
        return

    # 2. Open and load the current cart data
    try:
        cart = load_cart()
    except (FileNotFoundError, json.JSONDecodeError):
        cart = {} # Start fresh if the file doesn't exist or is empty

    # 3. Update the cart dictionary
    if item_name in cart:
        cart[item_name]["quantity"] += quantity

    # 4. Save the updated cart back to the cart.json file
        save_cart(cart)
    else:
        cart[item_name] = {
            "quantity": quantity, 
            "price_per_unit": found_item["price"]
        }
          
    print(f"Success: Added {quantity}x '{item_name}' to your cart!")
