import numpy as np

# Take input from the user for the size of the plus sign
size = int(input("Enter the size of the plus sign: "))


# Create an empty array filled with zeros
array = np.zeros((size, size), dtype=int)

# Fill the middle row and middle column with ones
middle = size // 2
array[middle, :] = 1
array[:, middle] = 1

print(array)
