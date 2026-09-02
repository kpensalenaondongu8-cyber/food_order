import json


def Food_Menu():
    try:
       
        with open("menu.json", "r") as file:
            menu = json.load(file)
            
        print("\n--- FOOD MENU ---")
        for food, info in menu.items():
           
            print(f"Food: {food:<10} | Price: ₦{info[1]:.2f} | Stock: {info[0]}")
        print("-------------------------\n")
        
    except FileNotFoundError:
        print("Error: menu.json file could not be found!")