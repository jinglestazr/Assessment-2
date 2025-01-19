# Displaying a Intro Screen for the Vending Machine 
def display_vending_machine_title():
    print("╔" + "═" * 46 + "╗")
    print("║           ~*~ SNACK STATION ~*~              ║")
    print("║         Your Favorite Snack Hub!             ║")
    print("╠" + "═" * 46 + "╣")
    print("║               A       B       C       D      ║")
    print("║             ---------------------------      ║")
    print("║     1      Water   Chips   Soda   Chocolate  ║")
    print("║     2      Juice   Cookies Energy Bar Muffins║")
    print("╚" + "═" * 46 + "╝\n")

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

# Displaying the menu in a readable format
def display_menu(items):
    print("\nAvailable Items:")
    for code, item in items.items():
        print(f"{code}: {item['name']} - {item['price']:.2f} dhs (Stock: {item['stock']})")

# Making it User interactive for the uswer to select the item of choice 
def get_item_code(items):
    while True:
        code = input("\nEnter the code of the item you want to purchase (e.g., 1A): ").upper()
        if code in items:
            return code
        print("Invalid code. Please try again.")
