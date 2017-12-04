# Method 1 : brute force
def is_palindrome(number):
    #using string
    return str(number) == str(number)[::-1]

max = 0
for i in range(1000):
    for j in range(1000):
        prod = i * j
        if prod > max and is_palindrome(prod):
            max = prod

print(max)
