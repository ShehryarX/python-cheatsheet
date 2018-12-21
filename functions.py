# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create function
def sayHello(name = 'Shehryar'):
  '''
  Prints Hello and then name.
  '''
  print('Hello ' + name)

# Return value
def getSum(a, b):
  total = a + b
  return total

def addOneToNum(num):
  num += 1
  return num

sayHello('Bob')

numSum = getSum(1,2)
print(numSum)

num = 5
new_num = addOneToNum(num)
print(new_num)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2 : num1 + num2
print(getSum(4, 5))

addOneToNum = lambda num : num + 1
print(addOneToNum(14))