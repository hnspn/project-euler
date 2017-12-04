from collections import defaultdict

def is_prime(number):
  '''
    Test is a number is prime  
    The numerous manual tests at the begining of the function imporove performance  
    This implementation is inspired by [a SO answer](https://stackoverflow.com/a/15285588)
  '''
  if number == 2 or number == 3: return True
  if number < 2 or number % 2 == 0: return False
  if number < 9: return True
  if number % 3 == 0: return False
  limit = int(number ** 0.5) + 1 
  return not any(number % factor == 0 or \
                  number % (factor + 2) == 0\
                  for factor in range(5, limit, 6))

def prime_factors(number):
  factors = defaultdict(int)
  for factor in range(2, number):
    while number % factor == 0 and is_prime(factor):
      number //= factor
      factors[factor] += 1
    if number == 1:
      break
  return factors

print(prime_factors(600851475143))
