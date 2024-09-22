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
    if sort_order == 1:  # Ascending order
        sorted_products = sorted(products_list, key=lambda x: x[1])
    elif sort_order == 2:  # Descending order
        sorted_products = sorted(products_list, key=lambda x: x[1], reverse=True)
    else:
        print("Invalid sort order. Displaying products as is.")
        sorted_products = products_list
    
    # Display sorted products
    for index, product in enumerate(sorted_products, start=1):
        print(f"{index}. {product[0]} - ${product[1]}")

def display_products(products_list):
    for index, product in enumerate(products_list, start=1):
        print(f"{index}. {product[0]} - ${product[1]}")

def display_categories():
    for index, category in enumerate(products.keys(), start=1):
        print(f"{index}. {category}")

def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))

def display_cart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        print("Your Shopping Cart:")
        total_cost = 0
        for item in cart:
            product_name, price, quantity = item
            total_cost += price * quantity
            print(f"{product_name} - ${price} x {quantity}")
        print(f"Total Cost: ${total_cost:.2f}")

def generate_receipt(name, email, cart, total_cost, address):
    if cart:
        print(f"Name: {name}")
        print(f"Email: {email}")
        print("Products Purchased:")
        for item in cart:
            product_name, price, quantity = item
            print(f"{product_name} - ${price} x {quantity}")
        print(f"Total Cost: ${total_cost:.2f}")
        print(f"Delivery Address: {address}")
        print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")
    else:
        print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")

def validate_name(name):
    parts = name.split()
    if len(parts) != 2:
        return False
    for part in parts:
        if not part.isalpha():
            return False
    return True

def validate_email(email):
    if '@' in email:
        return True
    return False

def main():
    print("Welcome to the Online Shopping Portal!")
    name = input("Please enter your name: ")
    while not validate_name(name):
        print("Invalid name format. Please enter your first and last name only, using alphabets.")
        name = input("Please enter your name: ")

    email = input("Please enter your email address: ")
    while not validate_email(email):
        print("Invalid email address. Please enter a valid email address.")
        email = input("Please enter your email address: ")

    print("Welcome,", name.split()[0], "!")

    while True:
        print("\nCategories Available:")
        display_categories()
        try:
            category_choice = int(input("\nEnter the number of the category you would like to explore: "))
            if category_choice < 1 or category_choice > len(products):
                print("Invalid category number. Please enter a valid category number.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid category number.")
            continue

        selected_category = list(products.keys())[category_choice - 1]
        print(f"\nProducts available in '{selected_category}':")
        display_products(products[selected_category])

        while True:
            print("\nOptions:")
            print("1. Select a product to buy")
            print("2. Sort the products according to the price")
            print("3. Go back to the category selection")
            print("4. Finish shopping")

            try:
                option = int(input("Enter your choice: "))
                if option < 1 or option > 4:
                    print("Invalid option. Please enter a valid option number.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid option number.")
                continue

            if option == 1:
                try:
                    product_choice = int(input("Enter the number corresponding to the product: "))
                    selected_product = products[selected_category][product_choice - 1]
                    quantity = int(input("Enter the quantity you want to buy: "))
                    add_to_cart(cart, selected_product, quantity)
                    print("Product added to cart.")
                except (IndexError, ValueError):
                    print("Invalid input. Please enter valid product and quantity.")
                    continue

            elif option == 2:
                try:
                    sort_order = int(input("Sort by price: 1. Ascending, 2. Descending: "))
                    if sort_order not in [1, 2]:
                        print("Invalid sort order. Please enter either 1 or 2.")
                        continue
                    print(f"\nProducts sorted by price ({'Ascending' if sort_order == 1 else 'Descending'}):")
                    display_sorted_products(products[selected_category], sort_order)
                except ValueError:
                    print("Invalid input. Please enter either 1 or 2 for sort order.")
                    continue

            elif option == 3:
                break  # Go back to category selection

            elif option == 4:
                print("\nYour Shopping Cart:")
                display_cart(cart)
                if cart:
                    total_cost = sum(item[1] * item[2] for item in cart)
                    address = input("Enter your delivery address: ")
                    generate_receipt(name, email, cart, total_cost, address)
                else:
                    generate_receipt(name, email, cart, 0, "")
                return

if __name__ == "__main__":
    main()
