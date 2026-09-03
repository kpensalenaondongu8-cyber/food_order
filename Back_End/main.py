from view_menu import display_Menu
from add_to_cart import add_to_cart 
from remove_from_cart import Rem_Fro_Cart
# from modify_cart import modify_cart
from view_cart import View_Cart
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
        rem_item = input("Enter item: ")
        Rem_Fro_Cart(item_x) 
    
    elif user_input == 4:
        item_mod = input("Enter item: ")
        print("--- Actions ---\n 1.Increase\n 2.Decrease")
        action = input("Enter action:")
        
        modify_cart(item_mod, action)

    elif user_input == 5:
        View_Cart()
    
    elif user_input == 7:
         
    elif user_input == 7:
        exit()
        break         



