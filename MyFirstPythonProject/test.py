# самое большое чаще других встречающееся число

def most_frequent_number(n, a):
  frequency = {}

  for num in a:
    if num in frequency:
      frequency[num] += 1
    else:
      frequency[num] = 1

  max_count = 0
  result = 0

  for num, count in frequency.items():
    if count > max_count or (count == max_count and num > result):
      max_count = count
      result = num
  return result


n = int(input())
a = list(map(int, input().split()))

result = most_frequent_number(n, a)
print(result)

  


# максимально общее начало каждого слова в списке
"""""""""""""""""
def longest_common_prefix(words):
  if not words:
    return ""

  prefix = words[0]

  for word in words[1:]:
    while not word.startswith(prefix):
      prefix = prefix[:-1]
      if not prefix:
        return ""
  return prefix

words = ["gina", "girls", "girl"]

print(longest_common_prefix(words))

"""""""""""""""


# common elements from 2 lists
"""""""""""""""""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common_elements = list(set(a) & set(b))

print(common_elements)
"""""""""""""""""

# all number lesser than 5
"""""""""""""""""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

result = [x for x in a if x < 5]

print(result)

"""""""""""""""""



# primary numbers seeking
"""""""""""""""""
def is_prime(num):
  if num < 2:
      return False
  for i in range(2, int(num ** 0.5) + 1):
      if num % i == 0:
        return False
  return True


def first_n_primes(n):
  primes = []
  num = 2
  while len(primes) < n:
    if is_prime(num):
      primes.append(num)
    num += 1
  return primes
      

print(first_n_primes(20))
"""""""""""""""


# Factorial seeking
#def factorial(n):
#  if n < 0:
#    return "Factorial is not defined for negative numbers"
#  elif n == 0 or n == 1:
#    return 1
#  else:
#    fact = 1
#   for i in range(2, n + 1):
#      fact *= i
#   return fact
#
#number = int(input("Enter a number: "))
#result = factorial(number)
#print(f"The factorial of {number} is {result}")
