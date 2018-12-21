# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1,2,3,4,5]

# Using constructor
numbers = list((1,2,3,4,5))

print(type(numbers))

fruits = ['Apples', 'Oranges', 'Grapes', 'Pears', 123]

# Get value
print(fruits[4]);

# Get length
print(len(fruits))

# Append to list
fruits.append('Mangoes')

# Remove from list
fruits.remove('Grapes')

# Insert into position
fruits.insert(2, 'Strawberries')

# Remove from position
fruits.pop(3)

# Reverse
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)