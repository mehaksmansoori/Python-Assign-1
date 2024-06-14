#Write a python program that returns the minimum and maximum values in a list of numbers. 
def find_min_max(number_list):
  if not number_list:
    raise ValueError("The list cannot be empty.")
  min_value = min(number_list)
  max_value = max(number_list)

  return min_value, max_value

number_list = [1, 5, 0, 2, 3]
min_value, max_value = find_min_max(number_list)
print(f"Minimum value: {min_value}, Maximum value: {max_value}")
