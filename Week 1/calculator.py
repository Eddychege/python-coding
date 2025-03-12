def calculator():
    # Get the user's input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the operation based on user input
    if operation == "+":
        result = num1 + num2
        operation = "addition"
    elif operation == "-":
        result = num1 - num2
        operation = "subtraction"
    elif operation == "*":
        result = num1 * num2
        operation = "multiplication"
    elif operation == "/":
        # Check for division by zero
        if num2 == 0:
            print("Cannot divide by zero")
            return
        result = num1 / num2
        operation = "division"
    else:
        print("Invalid operation. PLease use one of the following: +, -, *, /")
        return

    # Print the result
    print(f"{num1} {operation} {num2} = {result}")

# Call the calculator function
if __name__ == "__main__":
    print("Hello World!")
    print("Welcome to my simple calculator")
    print("--------------------------------------")
    calculator()