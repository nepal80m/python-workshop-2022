# Lambda function

from functools import reduce


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_only_list = []


def determine_if_num_is_even(num):
    return num % 2 == 0
# lambda num: num % 2 == 0


for num in numbers:
    if determine_if_num_is_even(num):
        even_only_list.append(num)

print(even_only_list)

print(list(filter(determine_if_num_is_even, numbers)))
# print(list(filter(lambda num: num % 2 == 0, numbers)))  # using lambda


print(type(determine_if_num_is_even))
# CALL BACK FUNCTION


# LAMBDA


# Syntax of filter
# filter(function,iterable)


# print(determine_if_num_is_even(111))

# filter(determine_if_num_is_even, numbers)


names = ['Kushal', 'Subash', 'Monika', 'Seeru', 'Tulasi', 'Buddhaa']
truth_name = [False, False, False, True, False, True]


def function_name(name):
    # name='Kushal'
    return len(name) % 2 != 0


filter(lambda name: len(name) % 2 != 0, names)

# use filter and lambda function
# only_names_with_odd_number_of_chars = ['Seeru', 'Buddhaa']


# map()
# map(function,iterable)

numbers = [1, 2, 3, 4, 5]

print(map(lambda num: num**2, numbers))
print(list(map(lambda num: num**2, numbers)))


# reduce()
# MAP
names = ['Kushal', 'Subash', 'Monika', 'Seeru', 'Tulasi', 'Buddhaa']
# Question 1
truth_name = [False, False, False, True, False, True]

# Question 2
truth_name = ["Even", "Even", "Even", "Odd", "Even", "Odd"]

# Question 3
# truth_name = ["L-A-H-S-U-K", ....]

print(list(map(lambda name: len(name) % 2 != 0, names)))


# FILTER
# REDUCE


# numbers

# reduce(function, iterable)
print(reduce(lambda a, b: a+b, [2, 3, 4, 5], 5))

# print(reduce((lambda a, b:  a+b), [1, 2, 3, 4, 5]))
print(reduce((lambda a, b:  a if a > b else b), [-1, -2, -3, -4, -5]))
