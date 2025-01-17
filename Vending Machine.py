# Display a Intro Screen for the Vending Machine
def display_vending_machine_title():
    print("+" + "-" * 32 + "+")
    print("|      Snackstation Vending      |")
    print("|          Machine Menu          |")
    print("+" + "-" * 32 + "+")
    print("         A   B   C   D")
    print("       -----------------")
    print("   1   Water   Chips   Soda   Chocolate")
    print("   2   Juice   Cookies Energy Bar Muffins")
    print("+" + "-" * 29 + "+\n") 

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

