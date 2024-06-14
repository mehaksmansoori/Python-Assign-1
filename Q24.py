#Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.
def calculate(num1, num2, operator):
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    if num2 == 0:
      raise ZeroDivisionError("Division by zero is not allowed.")
    return num1 / num2
  else:
    raise ValueError("Invalid operator. Please use +, -, *, or /.")

def get_user_input():
  while True:
    try:
      num1 = float(input("Enter the first number: "))
      num2 = float(input("Enter the second number: "))
      operator = input("Enter an operator (+, -, *, /): ")
      return num1, num2, operator
    except ValueError:
      print("Invalid input. Please enter numeric values and a valid operator (+, -, *, /).")

def main():
  try:
    num1, num2, operator = get_user_input()
    result = calculate(num1, num2, operator)
    print(f"The result of {num1} {operator} {num2} is: {result}")
  except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()
