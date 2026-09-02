from Food_menu import Food_Menu
from add_to_cart import Add_to_Cart
from remove_from_cart import Remove_From_Cart 




print("Select an Option: 1. Food_Menu 2.Add_to_Cart 3.Remove_From_Cart 4.Modify_Quantity 5.View_cart 6.Checkout")

while True:
    try:
        user_input = int(input("Select Operation: "))
    except ValueError:
        print("Invalid Syntax! Please enter a number.")
        continue    

    if user_input == 1:
        Food_Menu() 

    elif user_input == 2:
        item = input("Enter Item: ")
        try:
            quantity = int(input("Enter Quantity: "))
        except ValueError:
            print("Invalid Syntax")  
            continue
        Add_to_Cart(item, quantity)    
    elif user_input == 3:
        item = input("Enter Item: ")
        Remove_From_Cart(item)
        
