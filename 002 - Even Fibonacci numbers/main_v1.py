def fibonnaci(num, mem={0:0, 1:1}):
  '''
    This version of fibonnaci uses a dictionary to save the results of the recursive calls of the function.  
    The function is called by the user without specifying the **mem** parameter.  
    The **mem** dictionary is initialized with the base cases of the function.  
  '''
  if num not in mem:
    mem[num] = fibonnaci(num - 1, mem) + fibonnaci(num - 2, mem)
  return mem[num]

sum = 0
for num in range(100):
  temp = fibonnaci(num)
  if temp > 4000000:
    break
  if temp % 2 == 0:
    sum += temp

print(sum)
