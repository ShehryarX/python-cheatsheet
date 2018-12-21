# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open('myFile.txt', 'w') # write

# Get some info
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I love Python')
myFile.write(' and Javascript')

myFile.close()

# Append to file
myFile = open('myFile.txt', 'a') # append
myFile.write(' I also like PHP')
myFile.close()

# Read from file
myFile = open('myFile.txt', 'r+') # read
text = myFile.read(10)
print(text)