#Write a program that takes a string input from the user and writes it to a text file.
text_to_write = input("Enter the text you want to write to the file: ")

# Open the file in write mode
with open("user_input.txt", "w") as text_file:
  # Write the text to the file
  text_file.write(text_to_write)

print("Text written to file!")
