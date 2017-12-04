def is_palindrome(number):
    #using string
    return str(number) == str(number)[::-1]


palindromes = []

for a in range(100, 1000):
    for b in range(100, 1000):
        if a % 11 == 0 or b % 11 == 0:
            product = a * b
            if is_palindrome(product):
                palindromes.append(product)

print(*palindromes, sep='\n')
print(max(palindromes))
