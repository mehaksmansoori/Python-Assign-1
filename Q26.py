#Write a program in python that checks if a string starts with a given prefix or ends with a given suffix. 
def check_prefix_suffix(text, prefix, suffix):
  starts_with_prefix = False
  ends_with_suffix = False

  if prefix:
    starts_with_prefix = text.startswith(prefix)

  if suffix:
    ends_with_suffix = text.endswith(suffix)

  return starts_with_prefix, ends_with_suffix
text = "This is a python code with prefix and suffix."
prefix = "This"
suffix = "suffix."

is_prefix, is_suffix = check_prefix_suffix(text, prefix, suffix)

if is_prefix and is_suffix:
  print(f"'{text}' starts with '{prefix}' and ends with '{suffix}'.")
elif is_prefix:
  print(f"'{text}' starts with '{prefix}'.")
elif is_suffix:
  print(f"'{text}' ends with '{suffix}'.")
else:
  print(f"'{text}' does not start with '{prefix}' or end with '{suffix}'.")
