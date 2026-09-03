from view_menu import display_Menu
from add_to_cart import add_to_cart 
from remove_from_cart import Rem_Fro_Cart
from modify_cart import modify_cart
from view_cart import View_Cart
from checkout import checkout
from exit import exit

print("----- select transaction -----\n 1.View_Menu.\n 2.Add_To_Cart.\n 3.Remove_From_Cart.\n 4.Modify_Cart.\n 5.View_Cart.\n 6.Checkout.\n 7.Exit")

while True:
    try:
       user_input = int(input("Enter Operation: "))
    except ValueError:
       print("Invalid Syntax! Select the digits")
       continue
    if user_input == 1:
       display_Menu()

    elif user_input == 2:
       item_input = input("Enter Item: ")
       try:
          item_quantity = int(input("Enter Amount: "))
       except ValueError:
          print("Invalid syntax! Amount must be numbers")
          continue
       add_to_cart(item_input, item_quantity)

    elif user_input == 3:
      # .title() automatically converts "garlic bread" -> "Garlic Bread"
      rem_item = input("Enter item: ").strip().title()
      Rem_Fro_Cart(rem_item) 
    
    elif user_input == 4:
        # Standardize the item name capitalization
        item_mod = input("Enter item: ").strip().title()
        
        print("--- Actions ---\n 1. Increase\n 2. Decrease")
        action_input = input("Enter action (number or word): ").strip().lower()
        
        # 1. Standardize the action input string
        if action_input == "1" or action_input == "increase":
            action = "increase"
        elif action_input == "2" or action_input == "decrease":
            action = "decrease"
        else:
            print("Invalid action selected!")
            continue

        # 2. Ask for the bulk amount (with error checking)
        amount_input = input("Enter amount to change (Press Enter for 1): ").strip()
        
        if amount_input == "":
            amount = 1  # Default to 1 if they just hit Enter
        else:
            try:
               amount = int(amount_input)
               if amount <= 0:
                  print("Amount must be a positive number!")
                  continue
            except ValueError:
                     print("Invalid syntax! Amount must be a number.")
                     continue
        
        # Pass both the corrected action and the bulk amount into the router!
        modify_cart(item_mod, action, amount)


    elif user_input == 5:
        View_Cart()
    
    elif user_input == 6:
         checkout()
    elif user_input == 7:
        exit()
        break         



