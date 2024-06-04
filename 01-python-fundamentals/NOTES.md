- Syntax for "constant" variable: MY_VAR, though it doesn't prevent any changes to it.

- defining functions:
  def my_function(x, y):
  result = x + y
  return result

print(my_function(4, 5))

- function does not run until called.
- function syntax ends when the next line is not indented.

- if statement
  x = 0
  if x > 10:
  print('great')

- else and elif statements
  if x > 10:
  add(4, 5)
  print('great')
  elif x < 0:
  print('neg')
  else:
  print('mid')

- Order of Operations
  if (not y == 3) and (x == 0) or y > 10:
  ...

- You can do nested if statements
  if ...:
  ...
  if ...:
  ...
  else ...:
  ...
  else:
  ...
-

- you can clean up nested statements

def f():
...

if ...:
...
if()
else:
...

- The while and For loops are very important fundamental loops

- the while loops keeps running as long as while is true.
  x = 123456
  while x > 1:
  print(x)
  print('out of loop')

- For Loop
  my_numbers = [1,2,3]
  for num in my_numbers:
  print(num)
  print('out of loop')

- index with arrays
  for i in range(0,5):
  print( i , my_numbers[i])

<!-- get the length of array -->

for i in range(0, len(my_numbers)):
print( i , my_numbers[i])
