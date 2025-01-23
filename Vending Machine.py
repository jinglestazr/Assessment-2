# Displaying a Intro Screen for the Vending Machine 

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


# Display the menu in a visually appealing format
def display_menu(items):
    print("\n╔" + "═" * 46 + "╗")
    print("║                 Available Items              ║")
    print("╠" + "═" * 46 + "╣")
    print("║ Code │       Item Name       │ Price │ Stock ║")
    print("╠" + "═" * 46 + "╣")
    for code, item in items.items():
        print(f"║ {code:<4} │ {item['name']:<19} │ {item['price']:<5.2f} │ {item['stock']:<6}  ║")
    print("╚" + "═" * 46 + "╝")


# Get valid code from the user
def get_item_code(items):
    while True:
        code = input("\nEnter the code of the item you want to purchase (e.g., 1A): ").upper()
        if code in items:
            return code
        print("Invalid code. Please try again.")


# Process payment
def process_payment(item):
    while True:
        try:
            amount = float(input(f"Insert money (Price: {item['price']:.2f} dhs): "))
            if amount >= item["price"]:
                return amount - item["price"]
            else:
                print(f"Not enough money. Please add {item['price'] - amount:.2f} dhs more.")
        except ValueError:
            print("Invalid input. Please insert a valid amount.")


# Dispense item
def dispense_item(item, change):
    item["stock"] -= 1
    print(f"\nDispensing {item['name']}...")
    print(f"Your change: {change:.2f} dhs.")
    print(f"Enjoy your {item['name']}!\n")


# Suggest an additional item
def suggest_item(items, selected_code):
    for code, item in items.items():
        if code != selected_code and item["stock"] > 0:
            return code, item
    return None, None


# Main function
def vending_machine(items):
    display_vending_machine_title()
    while True:
        display_menu(items)
        code = get_item_code(items)
        item = items[code]

        if item["stock"] > 0:
            change = process_payment(item)

            # Suggest an additional item before dispensing the main item
            suggested_code, suggested_item = suggest_item(items, code)
            if suggested_code:
                suggestion = input(f"Would you like to add {suggested_item['name']} for {suggested_item['price']:.2f} dhs? (yes/no): ").strip().lower()
                if suggestion == "yes":
                    if suggested_item["stock"] > 0:
                        try:
                            change = process_payment(suggested_item)
                            dispense_item(suggested_item, change)
                        except ValueError:
                            print("Invalid payment. Skipping suggested item.")
                    else:
                        print(f"Sorry, {suggested_item['name']} is out of stock.")

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


