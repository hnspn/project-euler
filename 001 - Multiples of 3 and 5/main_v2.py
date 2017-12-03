def multiples_of(factors, upper_bound):
  '''
  Returns the multiples of the all the numbers in the factors array below the bound
  :param factors : list of integers  
  :param upper_bound : the upper bound
  '''
  return (num for num in range(upper_bound) if any(num % factor == 0 for factor in factors))

print(sum(multiples_of([3, 5], upper_bound=1000)))
