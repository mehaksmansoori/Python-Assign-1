#Write a program that reads data from a CSV file and prints it to the console.
import csv
def read_and_print_csv(filename):
  try:
    with open(filename, 'r') as csv_file:
      csv_reader = csv.reader(csv_file)
      for row in csv_reader:
        print(', '.join(row))

  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")

filename = "your_csv_file.csv"

read_and_print_csv(filename)
