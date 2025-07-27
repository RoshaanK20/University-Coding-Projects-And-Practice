class ArithmeticOperations:
    def __init__(self, a, b):
        self.__a = a  # Private variable
        self.__b = b  # Private variable

    # Public method to set values
    def set_values(self, a, b):
        self.__a = a
        self.__b = b

    # Public method to get values
    def get_values(self):
        return self.__a, self.__b

    # Private method for addition
    def __add(self):
        return self.__a + self.__b

    # Private method for subtraction
    def __subtract(self):
        return self.__a - self.__b

    # Private method for multiplication
    def __multiply(self):
        return self.__a * self.__b

    # Private method for division
    def __divide(self):
        if self.__b != 0:
            return self.__a / self.__b
        else:
            return "Division by zero is not allowed"

    # Public methods to access private methods
    def perform_addition(self):
        return self.__add()

    def perform_subtraction(self):
        return self.__subtract()

    def perform_multiplication(self):
        return self.__multiply()

    def perform_division(self):
        return self.__divide()

def main():
    print("Welcome to the Arithmetic Operations Calculator!")
    while True:
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print("\nSelect operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exit")
            choice = input("Enter choice (1/2/3/4/5): ").strip()

            arithmetic = ArithmeticOperations(a, b)

            if choice == '1':
                print("Result:", arithmetic.perform_addition())
            elif choice == '2':
                print("Result:", arithmetic.perform_subtraction())
            elif choice == '3':
                print("Result:", arithmetic.perform_multiplication())
            elif choice == '4':
                print("Result:", arithmetic.perform_division())
            elif choice == '5':
                print("Exiting the calculator. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid operation.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()