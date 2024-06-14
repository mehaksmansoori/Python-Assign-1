#Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.
def read_lines_until_empty():
  """Reads multiple lines of input from the user until an empty line is entered and returns the lines as a list.

  Returns:
    A list containing all the lines entered by the user, excluding the empty line.
  """
  lines = []
  while True:
    line = input("Enter a line (or press Enter to finish): ")
    if not line:
      break
    lines.append(line)
  return lines

def main():
  """Prompts the user for input, reads lines, and prints them."""
  lines = read_lines_until_empty()
  if lines:
    print("Lines entered:")
    for line in lines:
      print(line)
  else:
    print("No lines entered.")

if __name__ == "__main__":
  main()
