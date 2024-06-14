#Write a program that copies the contents of one text file to another. 
def copy_file(source_file, destination_file):
  with open(source_file, 'r') as source:
    with open(destination_file, 'w') as destination:
      for line in source:
        destination.write(line)

source_file = "source.txt"
destination_file = "copy.txt"
copy_file(source_file, destination_file)
print(f"Contents of '{source_file}' copied to '{destination_file}'.")
