def is_narcissistic(number):
    digits = str(number)
    num_digits = len(digits)
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    return sum_of_powers == number
num = int(input("Enter a number to check if it is narcissistic: "))
if is_narcissistic(num):
    print(f"{num} is a Narcissistic number.")
else:
    print(f"{num} is not a Narcissistic number.")
