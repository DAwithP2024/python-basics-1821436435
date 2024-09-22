# Products available in the store by category 
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_sorted_products(products_list, sort_order):
    if sort_order == "asc":  # Ascending order
        sorted_products = sorted(products_list, key=lambda x: x[1])
    elif sort_order == "desc":  # Descending order
        sorted_products = sorted(products_list, key=lambda x: x[1], reverse=True)
    return sorted_products


def display_products(products_list):
    for index, product in enumerate(products_list, start=1):
        print(f"{index}. {product[0]} - ${product[1]}")


def display_categories():
    for index, category in enumerate(products.keys(), start=1):
        print(f"{index}. {category}")
    
    category_choice = input("Enter the number of the category: ")
    try:
        category_index = int(category_choice) - 1
        if category_index < 0 or category_index >= len(products):
            print("Invalid category number.")
            return None
        return category_index
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return None


def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))


def display_cart(cart):
    total_cost = 0
    if cart:
        for item in cart:
            product_name, price, quantity = item
            cost = price * quantity
            print(f"{product_name} - ${price} x {quantity} = ${cost}")
            total_cost += cost
        print(f"Total cost: ${total_cost}")
    else:
        print("Your cart is empty.")


def generate_receipt(name, email, cart, total_cost, address):
    print(f"Customer: {name}")
    print(f"Email: {email}")
    print("Items Purchased:")
    for item in cart:
        product_name, price, quantity = item
        cost = price * quantity
        print(f"{quantity} x {product_name} - ${price} = ${cost}")
    print(f"Total: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days. Payment will be accepted upon delivery.")


def validate_name(name):
    parts = name.split()
    if len(parts) != 2:
        return False
    return all(part.isalpha() for part in parts)


def validate_email(email):
    return '@' in email and email.strip() != ""


def main():
    cart = []

    # Welcome message
    print("Welcome to the Online Shopping Portal!")
    name = input("Please enter your name: ")
    while not validate_name(name):
        print("Invalid name format. Please enter your first and last name only, using alphabets.")
        name = input("Please enter your name: ")

    email = input("Please enter your email address: ")
    while not validate_email(email):
        print("Invalid email address. Please enter a valid email address.")
        email = input("Please enter your email address: ")

    print(f"Welcome, {name.split()[0]}!")

    while True:
        print("\nCategories Available:")
        category_index = display_categories()
        if category_index is None:
            continue
        
        selected_category = list(products.keys())[category_index]
        print(f"\nProducts available in '{selected_category}':")
        display_products(products[selected_category])

        while True:
            print("\nOptions:")
            print("1. Select a product to buy")
            print("2. Sort the products according to the price")
            print("3. Go back to the category selection")
            print("4. Finish shopping")

            option = input("Enter your choice: ")
            if option == "1":
                product_choice = input("Enter the number corresponding to the product: ")
                try:
                    product_index = int(product_choice) - 1
                    selected_product = products[selected_category][product_index]
                    quantity = input("Enter the quantity you want to buy: ")
                    if not quantity.isdigit() or int(quantity) <= 0:
                        print("Invalid quantity. Please enter a positive number.")
                        continue
                    add_to_cart(cart, selected_product, int(quantity))
                    print("Product added to cart.")
                except (IndexError, ValueError):
                    print("Invalid product selection. Please try again.")
            elif option == "2":
                sort_order = input("Sort by price: 'asc' for ascending, 'desc' for descending: ").strip()
                if sort_order in ["asc", "desc"]:
                    sorted_products = display_sorted_products(products[selected_category], sort_order)
                    display_products(sorted_products)
                else:
                    print("Invalid sort order. Please enter 'asc' or 'desc'.")
            elif option == "3":
                break  # Go back to category selection
            elif option == "4":
                total_cost = sum(item[1] * item[2] for item in cart)
                display_cart(cart)
                if cart:
                    address = input("Enter your delivery address: ")
                    generate_receipt(name, email, cart, total_cost, address)
                else:
                    print("Thank you for using our portal. Hope you buy something next time.")
                return
            else:
                print("Invalid option. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()