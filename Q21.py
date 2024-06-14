#Write a python program that counts the occurrences of a specific element in a list.
def count_occurrences(data_list, element):
  count = 0
  for item in data_list:
    if item == element:
      count += 1
  return count

my_list = [1, 2, 4, 5, 5, 7, 9, 7]
element_to_count = 2
number_of_occurrences = count_occurrences(my_list, element_to_count)
print(f"The element {element_to_count} appears {number_of_occurrences} times in the list.")
