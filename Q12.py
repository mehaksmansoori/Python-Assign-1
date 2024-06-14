#Write a python program that calculates the sum of the digits of a given number.
def sum_of_digits(number):
  if number == 0:
    return 0
  if number < 0:
    number = abs(number)

  sum = 0
  while number > 0:
    last_digit = number % 10
    sum += last_digit
    number //= 10

  return sum
number = 1987
digit_sum = sum_of_digits(number)
print(f"The sum of digits in {number} is: {digit_sum}")
