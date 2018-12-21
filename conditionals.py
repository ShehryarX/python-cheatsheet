# If/ Else conditions are used to decide to do something based on something being true or false

x = 10
y = 6

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple if
if x == y:
  print('{} is equal to {}'.format(x, y))

# If/else
if x > y:
  print('{} is greater than {}'.format(x,y))
else:
  print('{1} is greater than {0}'.format(x,y))

# elif
# If/else
if x > y:
  print('{} is greater than {}'.format(x,y))
elif x == y:
  print('{} is equal to {}'.format(x,y))
else:
  print('{1} is greater than {0}'.format(x,y))

# Nested if
if x > 2:
  if x <= 10:
    print('{} is between 3 and 10'.format(x))


# Logical operators (and, or, not) - Used to combine conditional statements

# and
if x > 2 and x <= 10:
  print('{} is between 3 and 10'.format(x))

# or
if x > 2 or x <= 10:
  print('{} is between 3 and 10'.format(x))

# not
if not(x == y):
  print('{} is not equal to {}'.format(x,y))

# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1,2,3,4,5,6]

# in
if y in numbers:
  print(y in numbers)

# not in
if x not in numbers:
  print(x not in numbers)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
if x is y:
  print(x is y)

if x is not y:
  print(x is not y)