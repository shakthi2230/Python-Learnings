def is_armstrong_number(number):
    # Convert the number to a string to find the number of digits
    num_str = str(number)
    num_digits = len(num_str)
    
    # Calculate the sum of digits raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum is equal to the original number
    return armstrong_sum == number

# Example usage:
number_to_check = int(input("Enter a number to check for Armstrongness: "))
if is_armstrong_number(number_to_check):
    print(f"{number_to_check} is an Armstrong number.")
else:
    print(f"{number_to_check} is not an Armstrong number.")
