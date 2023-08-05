# Task 1: Hello, World!
print("Hello, World!")

# Task 2: Data Type Play
var_integer = 10
var_float = 3.14
var_string = "Hello, Python!"
var_boolean = True
var_list = [1, 2, 3, 4]
var_tuple = (5, 6, 7, 8)
var_dictionary = {'a': 1, 'b': 2, 'c': 3}
var_set = {9, 10, 11}

data_types = [
    var_integer,
    var_float,
    var_string,
    var_boolean,
    var_list,
    var_tuple,
    var_dictionary,
    var_set
]

for data in data_types:
    print(f"Type of variable: {type(data)}, value: {data}")

# Task 3: List Operations
numbers_list = list(range(1, 11))
print("Original list:", numbers_list)

# Add a number
numbers_list.append(20)
print("After adding 20:", numbers_list)

# Remove a number
numbers_list.remove(5)
print("After removing 5:", numbers_list)

# Sort the list
numbers_list.sort()
print("Sorted list:", numbers_list)

# Task 4: Sum and Average
def calculate_sum_and_average(num_list):
    total_sum = sum(num_list)
    average = total_sum / len(num_list)
    return total_sum, average

input_list = [10, 20, 30, 40]
sum_result, average_result = calculate_sum_and_average(input_list)
print(f"Sum: {sum_result}, Average: {average_result}")


# Task 5: String Reversal
def reverse_string(input_string):
    return input_string[::-1]

input_string = "Python"
output_string = reverse_string(input_string)
print(output_string)

# Task 6: Count Vowels
def count_vowels(input_string):
    vowels = "AEIOUaeiou"
    vowel_count = sum(1 for char in input_string if char in vowels)
    return vowel_count

input_string = "Hello"
vowel_count = count_vowels(input_string)
print(f"Number of vowels: {vowel_count}")

# Task 7: Prime Number
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

input_number = 13
if is_prime(input_number):
    print(f"{input_number} is a prime number.")
else:
    print(f"{input_number} is not a prime number.")

# Task 8: Factorial Calculation
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

input_number = 5
result = factorial(input_number)
print(f"Factorial of {input_number} is {result}.")

# Task 9: Fibonacci Sequence
def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

n = 5
fibonacci_sequence = fibonacci(n)
print(f"Fibonacci sequence with {n} numbers: {fibonacci_sequence}")
