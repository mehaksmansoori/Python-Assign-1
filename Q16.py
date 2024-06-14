#Write a program in python that counts the frequency of each character in a string.
def char_frequency(text):
  char_counts = {}
  for char in text:
    if char in char_counts:
      char_counts[char] += 1
    else:
      char_counts[char] = 1
  return char_counts

text = "Hello world! This is beautiful."
frequency_dict = char_frequency(text)
for char, count in frequency_dict.items():
  print(f"Character '{char}': {count}")
