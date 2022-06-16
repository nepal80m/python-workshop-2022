# IN C/C++
# for(int i=0;i<100;i++){}


# IN Python
# for range:
#   statement

# print(list(range(10)))  # default start from 0
# print(list(range(1, 10)))  # range
# print(list(range(1, 10, 2)))  # Step

# my_list = [1, 2, 3, 4, 5]
# my_string = 'Arun aka Suman'
# for char in my_string:
#     print(char)
students = [
    {"name": "Asim", "age": 22, "score": 20},
    {"name": "Nischal", "age": 23, "score": 30},
    {"name": "Blah", "age": 24, "score": 40},
]
# iterables: list, string, range
# for student in students:
# print(student)
# print(
#     f"I am {student['name']}. I am {student['age']}. I scored {student['score']}")

# for i in range(10):
#     print(i)

# Classwork 1
# create a new list with square
# HINT1: use list.append() function to add new items to the list
# HINT2: square of a is a**2
numbers = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
# squares = []
# for num in numbers:
#     squares.append(num**2)
# print(squares)


names = ['Asim', 'Nischal', 'Blah']
print(names)
print(list(enumerate(names)))

# ARGS, KWARGS


name = (0, 'Asim')
i, name = (0, 'Asim')

i, *name = (0, 'Asim', 'Nepal', [], False)

# print(i, name)
# Enumerate concepts
for i, name in enumerate(names):
    print(i, name)

# To find the lenght of any iterable:
# len(square)
# len(range(10))

# Classwork 2
# print true if all the numbers in the list are even.

# Classwork 3
# Determine if all the numbers in the list are


# numbers = [1, 2, 3, 4, 5, 6, 8]
# # squares = [1, 4, 9, 16, 25]
# squares = []
# for num in numbers:
#     if num % 2 == 0:
#         squares.append(num**2)
# print(squares)

# # List Comprehension
# # squares = [num**2 for num in numbers]
# squares = [num**2 for num in numbers if num % 2 == 0]

# print(squares)
