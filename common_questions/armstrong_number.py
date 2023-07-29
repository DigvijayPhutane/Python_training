def is_armstrong_number(number):
    num = number
    total_digits = len(str(number))
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit ** total_digits
        num //= 10
    if sum == number:
        return True
    else:
        return False

# Example usage
number = int(input("Enter a number: "))
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")