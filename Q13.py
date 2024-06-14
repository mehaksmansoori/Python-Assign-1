#Write a program that asks the user for their birth year and calculates their age. 
import datetime

def calculate_age(birth_year):
  current_year = datetime.date.today().year
  age = current_year - birth_year
  return age

def main():
  try:
    birth_year = int(input("Enter your birth year: "))
    age = calculate_age(birth_year)
    print(f"Your age is: {age}")
  except ValueError:
    print("Invalid input. Please enter a valid year.")

if __name__ == "__main__":
  main()
