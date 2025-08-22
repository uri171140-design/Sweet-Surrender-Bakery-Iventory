
def key(name: str) -> str:
    """Normalize names so 'Flour' and 'flour' are treated the same."""
    return name.strip().lower()

def input_float(prompt: str) -> float:
    """Ask the user for a non-negative number; keep retrying until valid."""
    while True:
        s = input(prompt).strip()
        try:
            value = float(s)
            if value < 0:
                print("Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number (e.g., 2 or 2.5).")

def add_ingredient(inventory: dict) -> None:
    """Add a new ingredient or replace an existing one."""
    name = input("Ingredient name (e.g., Flour): ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    unit = input("Unit (e.g., kg, litres, pieces): ").strip()
    if not unit:
        print("Unit cannot be empty.")
        return

    qty = input_float("Quantity: ")

    k = key(name)
    # If it already exists, confirm before replacing
    if k in inventory:
        ans = input(f"'{inventory[k]['name']}' exists. Replace with new details? (y/n): ").strip().lower()
        if ans != "y":
            print("Cancelled.")
            return

    inventory[k] = {"name": name.strip().title(), "unit": unit.strip(), "quantity": qty}
    print("✅ Ingredient saved.")

def view_all(inventory: dict) -> None:
    """Show all ingredients and their quantities."""
    if not inventory:
        print("No ingredients yet.")
        return

    print("\nCurrent Ingredients")
    print("-" * 52)
    print(f"{'Name':20} {'Quantity':>12} {'Unit':>12}")
    print("-" * 52)
    for _, item in sorted(inventory.items()):
        print(f"{item['name']:20} {item['quantity']:12.2f} {item['unit']:>12}")
    print("-" * 52)

def use_ingredient(inventory: dict) -> None:
    """Subtract an amount from an ingredient (when bakers use it)."""
    name = input("Which ingredient did you use? ").strip()
    k = key(name)
    item = inventory.get(k)

    if not item:
        print("Ingredient not found.")
        return

    used = input_float(f"Amount used ({item['unit']}): ")
    # Never go below zero
    item["quantity"] = max(0.0, item["quantity"] - used)
    print(f"Updated. {item['name']} now {item['quantity']} {item['unit']}.")

def search_ingredient(inventory: dict) -> None:
    """Find an ingredient and show its quantity and unit."""
    name = input("Search ingredient name: ").strip()
    item = inventory.get(key(name))

    if not item:
        print("Ingredient not found.")
        return

    print(f"{item['name']}: {item['quantity']} {item['unit']}")

def menu() -> None:
    """Print the main menu."""
    print("""
Sweet Surrender Inventory
1) Add new ingredient
2) View all ingredients
3) Use ingredient (update quantity)
4) Search ingredient
5) Exit
""")

def main():
    # Our in-memory store for the session
    inventory = {}

    while True:
        menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_ingredient(inventory)
        elif choice == "2":
            view_all(inventory)
        elif choice == "3":
            use_ingredient(inventory)
        elif choice == "4":
            search_ingredient(inventory)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please choose 1–5.")

if __name__ == "__main__":
    main()