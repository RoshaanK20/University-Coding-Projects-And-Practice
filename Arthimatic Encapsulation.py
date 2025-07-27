class ArithmeticOperations:
    def __init__ (self, a, b):
        self.__a = a # Private Variable
        self.__b = b # Private Variable

    # Public Method for set_values
    def set_values(self, a, b):
        self.__a = a
        self.__b = b

    # Public Method for get_values
    def get_values(self):
        return self.__a, self.__b
    
    # Private Method for Addition (__add)
    def __add(self):
        return self.__a + self.__b
    
    # Private Method for Subtraction (__subtract)
    def __subtract(self):
        return self.__a - self.__b
    
    # Private Method for Multiplication (__multiply)
    def __multiply(self):
        return self.__a * self.__b
    
    # Private Method for Division (__divide)
    def __divide(self):
        if self.__b != 0:
            return self.__a / self.__b
        else: 
            return "Division by zero is not allowed"
    
    # Private Method for Modulo (__modulo)
    def __modulo(self):
        return self.__a % self.__b
    
    # Public Method for addition
    def perform_addition(self):
        return self.__add()
    
    # Public Method for subtraction
    def perform_substraction(self):
        return self.__subtract()
    
    # Public Method for multiplication
    def perform_multiplication(self):
        return self.__multiply()
    
    # Public Method for division
    def perform_division(self):
        return self.__divide()
    
    # Public Method for modulo
    def perform_modulo(self):
        return self.__modulo()
    
def main():
    print("Welcome To The MHR Calculator!")
    while True:
        try: 
            a= float(input("Enter The First Number: "))
            b= float(input("Enter The Second Number: "))
            calculate = ArithmeticOperations(a, b)

            print("\nSelect Operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Modulo")
            print("6. Exit")

            choice = input("Enter Desired Operation (1/2/3/4/5/6): ").strip()

            if choice == '1':
                print("Result:", calculate.perform_addition())
            elif choice == '2':
                print("Result:", calculate.perform_substraction())
            elif choice == '3':
                print("Result:", calculate.perform_multiplication())
            elif choice == '4':
                print("Result: ", calculate.perform_division())
            elif choice == '5':
                print("Result:", calculate.perform_modulo())
            elif choice == '6':
                print("Thank You For Using The MHR Calculator!")
                break
            else:
                print("Invalid choice. Please select number from 1-6!")
        except ValueError:
            print("Invalid Input. Please enter a numeric value!")

if __name__ == "__main__":
    main()
        


