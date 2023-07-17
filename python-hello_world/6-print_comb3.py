for tens_digit in range(10):
    for ones_digit in range(tens_digit + 1, 10):
        print(f"{tens_digit}{ones_digit}", end=", " if tens_digit < 8 else "\n")