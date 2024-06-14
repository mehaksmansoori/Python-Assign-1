#Write a program that reads the content of a text file and prints it to the console.
def read_and_print_file(filename):
  try:
    with open(filename, 'r') as file:
      contents = file.read()
      # Print the contents to the console
      print(contents)
  except FileNotFoundError:
      print(f"Error: File '{filename}' not found.")
filename = "your_text_file.txt"

read_and_print_file(filename)
