#Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input. 
def convert_temperature(temperature, scale):
  if scale.upper() == "C":
    return (temperature * 9/5) + 32
  elif scale.upper() == "F":
    return (temperature - 32) * 5/9
  else:
    raise ValueError("Invalid temperature scale. Please use 'C' or 'F'.")

def get_user_input():

  while True:
    try:
      temp_value = float(input("Enter temperature value: "))
      temp_scale = input("Enter temperature scale (C or F): ").upper()
      if temp_scale not in ("C", "F"):
        raise ValueError
      return temp_value, temp_scale
    except ValueError:
      print("Invalid input. Please enter a numeric temperature value and 'C' or 'F' for scale.")

def main():
  temperature, scale = get_user_input()
  converted_temp = convert_temperature(temperature, scale)

  if scale == "C":
    print(f"{temperature:.2f} degrees Celsius is equal to {converted_temp:.2f} degrees Fahrenheit.")
  else:
    print(f"{temperature:.2f} degrees Fahrenheit is equal to {converted_temp:.2f} degrees Celsius.")

if __name__ == "__main__":
  main()
