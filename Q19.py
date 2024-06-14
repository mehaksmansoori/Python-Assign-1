#Write a python program that removes all punctuation from a given string.
def remove_punctuation(text):
  punctuation = "!\"#$%&()*+, -./:;<=>?@[\]^_`{|}~"
  no_punct_table = str.maketrans('', '', punctuation)
  text_without_punct = text.translate(no_punct_table)

  return text_without_punct
text = "This is a string with  punctuation."
text_without_punct = remove_punctuation(text)
print(text_without_punct) 
