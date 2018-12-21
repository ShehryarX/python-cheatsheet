# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Simple tuple
fruit_tuple = ('Apple', 'Orange', 'Mango')

# Using constructor
fruit_tuple = tuple(('Apple', 'Orange', 'Mango'))

# Get single value
print(fruit_tuple[1])

# Cannot change value
# fruit_tuple[1] = 'Grape'

print(fruit_tuple)

# Tuples with one value should have trailing comma
fruit_tuple_2 = ('Apple',)

# Length
print(len(fruit_tuple_2))

print(fruit_tuple_2)

# Deletes
del fruit_tuple_2


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruit_set = {'Apple', 'Orange', 'Mango', 'Apple'}

# Check if in set
print('Apple' in fruit_set)

# Add to a set
fruit_set.add('Grape')

# Remove from set
fruit_set.remove('Grape')

# Clear set
fruit_set.clear()

print(fruit_set) 

del fruit_set