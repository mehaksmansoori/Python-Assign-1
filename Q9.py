#Write a python program that checks if a substring is present in a given string.
def is_substring_present(main_str, sub_str):
  return sub_str in main_str

main_string = "This is a string with a substring"
substring = "substring"
is_present = is_substring_present(main_string, substring)

if is_present:
  print(f"The substring '{substring}' is present in the string.")
else:
  print(f"The substring '{substring}' is not present in the string.")
