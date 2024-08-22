# Example: Sorting a list of strings alphabetically
words = ['banana', 'apple', 'cherry', 'date']
sorted_words = sorted(words)
print(sorted_words)  # Output: ['apple', 'banana', 'cherry', 'date']

# Example: Sorting a list of tuples based on the second element
data = [('John', 25), ('Alice', 30), ('Bob', 20)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # Output: [('Bob', 20), ('John', 25), ('Alice', 30)]

# Example: Filtering even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4, 6, 8, 10]


# Example 1: Doubling the numbers in a list using map
numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(lambda x: x * 2, numbers)
print(list(doubled_numbers))  # Output: [2, 4, 6, 8, 10]

# Example 2: Converting a list of integers to strings using map
numbers = [1, 2, 3, 4, 5]
string_numbers = map(str, numbers)
print(list(string_numbers))  # Output: ['1', '2', '3', '4', '5']

# Example: Lambda function to add two numbers
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8

