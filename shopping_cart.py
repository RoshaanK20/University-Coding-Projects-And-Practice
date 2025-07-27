class CartOperations:
    def calculate_total(self, items):
        return sum(item['price'] for item in items)

    def apply_discount(self, total, discount_percentage):
        return total - (total * discount_percentage / 100)

    def calculate_tax(self, total, tax_rate):
        return total + (total * tax_rate / 100)

    def split_bill(self, total, people):
        return total / people

# Class for calculations
class ShoppingCart:
    def __init__(self):
        self.operations = CartOperations()
        self.items = []  # Store items as a list of dictionaries

    def add_item(self):
        name = input("Enter the item name: ")
        while True:
            try:
                price = float(input(f"Enter the price for {name} (in PKR): "))
                if price < 0:
                    print("Price cannot be negative. Please enter a valid price.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for the price.")
                
        self.items.append({'name': name, 'price': price})
        print(f"Item '{name}' added to the cart.")

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
            return
        print("Items in your cart:")
        for item_number, cart_item in enumerate(self.items, start=1):
            print(f"{item_number}. {cart_item['name']} - PKR {cart_item['price']:.2f}")
        total = self.operations.calculate_total(self.items)
        print(f"Current total: PKR {total:.2f}")

    def apply_discount(self):
        if not self.items:
            print("Your cart is empty. Add items first.")
        else:
            while True:
                try:
                    discount = float(input("Enter discount percentage: "))
                    if discount < 0:
                        print("Discount cannot be negative. Please enter a valid discount.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value for the discount.")
                    
            total = self.operations.calculate_total(self.items)
            discounted_total = self.operations.apply_discount(total, discount)
            print(f"Price after discount: PKR {discounted_total:.2f}")

    def calculate_tax(self):
        if not self.items:
            print("Your cart is empty. Add items first.")
        else:
            while True:
                try:
                    tax_rate = float(input("Enter tax rate percentage: "))
                    if tax_rate < 0:
                        print("Tax rate cannot be negative. Please enter a valid tax rate.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value for the tax rate.")
                    
            total = self.operations.calculate_total(self.items)
            total_with_tax = self.operations.calculate_tax(total, tax_rate)
            print(f"Total price with tax: PKR {total_with_tax:.2f}")

    def split_bill(self):
        if not self.items:
            print("Your cart is empty. Add items first.")
        else:
            while True:
                try:
                    people = int(input("Enter number of people to split the bill: "))
                    if people <= 0:
                        print("Number of people must be at least 1.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value for the number of people.")
                    
            total = self.operations.calculate_total(self.items)
            each_share = self.operations.split_bill(total, people)
            print(f"Each person should pay: PKR {each_share:.2f}")

# Function taking input from user
def main():
    cart = ShoppingCart()

    while True:
        print("\n--- Shopping Cart Menu ---")
        print("1. Add item to cart")
        print("2. View cart")
        print("3. Apply discount")
        print("4. Calculate tax")
        print("5. Split the bill")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ")

        if choice == '1':
            cart.add_item()

        elif choice == '2':
            cart.view_cart()

        elif choice == '3':
            cart.apply_discount()

        elif choice == '4':
            cart.calculate_tax()

        elif choice == '5':
            cart.split_bill()

        elif choice == '6':
            print("Exiting the shopping cart.")
            break

        else:
            print("Invalid option. Please choose a number between 1 and 6.")

# To run the program
if __name__ == "__main__":
    main()
