def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount

    Args:
        price(float): The original price of the item
        discount_percent(float): The discount percentage

    Returns:
        float: The final price after discount (if applicable)
    """
    if discount_percent >= 20:
        # Apply the discount if it's 20% or higher
        discount_amount = price * discount_percent / 100
        final_price = price - discount_amount
        return final_price
    else:
        # Return original price if discount is less than 20%
        return price

def main():
    # Prompt user for input
    try:
        original_price = float(input("Enter the original price of the item: KShs"))
        discount_percent = float(input("Enter the discount percentage: "))

        # Validate inputs
        if original_price < 0 or discount_percent < 0:
            print("Error: Price and discount percentage cannot be negative")
            return

        # Calculate and display the final price:
        final_price = calculate_discount(original_price, discount_percent)

        # Output the result
        if final_price < original_price:
            print(f"Discount applied: {discount_percent}%")
            print(f"Final price: KShs. {final_price:.2f}")
        else:
            print("No discount applied")
            print(f"Price: KShs{original_price:.2f}")

    except ValueError:
        print("Error: Invalid input. Please enter a valid number for price and discount percentage")

# Run the program
if __name__ == "__main__":
    main()
