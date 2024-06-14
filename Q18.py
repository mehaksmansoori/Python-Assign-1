#Write a python program that checks if two strings are anagrams of each other.
def is_anagram(str1, str2):
  str1 = str1.lower()
  str2 = str2.lower()
  char_dict = {}
  for char in str1:
    if char not in char_dict:
      char_dict[char] = 0
    char_dict[char] += 1
  for char in str2:
    if char not in char_dict or char_dict[char] == 0:
      return False
    char_dict[char] -= 1
  return True

print(is_anagram("hello", "olleh")) 
print(is_anagram("hello", "pet")) 