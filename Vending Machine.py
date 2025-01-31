# Displaying a Title Screen for the Vending Machine
def display_vending_machine_title():
    print(r"""
███████╗███╗   ██╗ █████╗  ██████╗██╗  ██╗    ███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗
██╔════╝████╗  ██║██╔══██╗██╔════╝██║ ██╔╝    ████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝
███████╗██╔██╗ ██║███████║██║     █████╔╝     ██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗  
╚════██║██║╚██╗██║██╔══██║██║     ██╔═██╗     ██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝  
███████║██║ ╚████║██║  ██║╚██████╗██║  ██╗    ██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗
╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝
                                                                                                    
    """)
    print("╔" + "═" * 46 + "╗")
    print(r"║           ~*~ ͓͓̽̽S͓͓̽̽N͓͓̽̽A͓͓̽̽C͓͓̽̽K͓̽ ͓̽N͓͓̽̽A͓͓̽̽T͓͓̽̽I͓͓̽̽O͓͓̽̽N͓̽ ~*~               ║")
    print("║         Your Favorite Snack Hub!             ║")
    print("╠" + "═" * 46 + "╣\n")


# Displaying the menu in a table format for the user to identify it for visibly 
def display_menu(items):
    print("\n╔" + "═" * 46 + "╗")
    print("║                 Available Items              ║")
    print("╠" + "═" * 46 + "╣")
    print("║ Code │       Item Name     │ Price │ Stock   ║")
    print("╠" + "═" * 46 + "╣")
    for code, item in items.items():
        print(f"║ {code:<4} │ {item['name']:<19} │ {item['price']:<5.2f} │ {item['stock']:<6}  ║")
    print("╚" + "═" * 46 + "╝")


# Made a code for the user to input the item they want
def get_item_code(items):
    while True:
        code = input("\nEnter the code of the item you want to purchase (e.g., 1A): ").upper()
        if code in items:
            return code
        print("Invalid code. Please try again.")


# Code for the payment process 
def process_payment(item):
    total_paid = 0
    while total_paid < item["price"]:
        try:
            amount = float(input(f"Insert money (Remaining: {item['price'] - total_paid:.2f} dhs): "))
            if amount > 0:
                total_paid += amount
            else:
                print("Please insert a valid positive amount.")
        except ValueError:
            print("Invalid input. Please insert a valid amount.")
    return total_paid - item["price"]


# Code for Dispensing item to the user
def dispense_item(item, change):
    item["stock"] -= 1
    print(f"\nDispensing {item['name']}...")
    if change > 0:
        print(f"Your change: {change:.2f} dhs.")
    print(f"Enjoy your {item['name']}!\n")


# Suggesting an additional item for the user to purchase
def suggest_item(items, selected_code):
    for code, item in items.items():
        if code != selected_code and item["stock"] > 0:
            return code, item
    return None, None


# Main function for the items in the vending machine 
def vending_machine(items):
    display_vending_machine_title()
    while True:
        display_menu(items)
        code = get_item_code(items)
        item = items[code]

        if item["stock"] > 0:
            print(f"You selected {item['name']} for {item['price']:.2f} dhs.")
            change = process_payment(item)

            # Suggesting an additional item before dispensing the main item
            suggested_code, suggested_item = suggest_item(items, code)
            if suggested_code:
                suggestion = input(f"Would you like to add {suggested_item['name']} for {suggested_item['price']:.2f} dhs? (yes/no): ").strip().lower()
                if suggestion == "yes" and suggested_item["stock"] > 0:
                    print(f"You selected {suggested_item['name']}.")
                    additional_change = process_payment(suggested_item)
                    dispense_item(suggested_item, additional_change)

            dispense_item(item, change)

        else:
            print(f"\nSorry, {item['name']} is out of stock.\n")

        another = input("Do you want to buy another item? (yes/no): ").strip().lower()
        if another != "yes":
            print("\nThank you for using Snackstation Vending Machine. Goodbye!")
            break


# Vending Machine Items
items = {
    "1A": {"name": "Water", "price": 1.00, "stock": 5},
    "1B": {"name": "Chips", "price": 1.50, "stock": 5},
    "1C": {"name": "Soda", "price": 2.00, "stock": 5},
    "1D": {"name": "Chocolate", "price": 2.50, "stock": 5},
    "2A": {"name": "Juice", "price": 2.00, "stock": 5},
    "2B": {"name": "Cookies", "price": 1.75, "stock": 5},
    "2C": {"name": "Energy Bar", "price": 3.00, "stock": 5},
    "2D": {"name": "Muffins", "price": 2.25, "stock": 5},
}


# Start the vending machine process
vending_machine(items)


