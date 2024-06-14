#Write a python program that generates the first n numbers in the Fibonacci sequence. 
def fibonacci_sequence(n):
  if n < 0:
    return []
  elif n == 0:
    return [0]
  elif n == 1:
    return [0, 1]
  fibonacci_list = [0, 1]
  for i in range(2, n):
    next_number = fibonacci_list[i-1] + fibonacci_list[i-2]
    fibonacci_list.append(next_number)

  return fibonacci_list

number_of_terms = 5
fibonacci_numbers = fibonacci_sequence(number_of_terms)
print(f"The first {number_of_terms} Fibonacci numbers are: {fibonacci_numbers}")
