# Functions for basic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero!"

# Calculator interface
def calculator():
    print("Select the operation:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")

    while True:
        # Receives user input
        choice = input("Enter your choice (1/2/3/4): ")

        # Checks if the choice is valid
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {adicionar(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtrair(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {dividir(num1, num2)}")
            
            # Asks the user if they want to continue
            nextcount = input("Do you want to perform another operation? (y/n): ")
            if nextcount.lower() != 'y':
                break
        else:
            print("Invalid option. Try again.")

# Run the calculator
calculator()