# Useful Shortcuts

# Move code UPDOWN: Alt+ Arrow up down
# Copy up down : Shift + ALT + Arrow up down
# Line select: Ctrl+L
# Line delete: Ctrl+X
# Highlight multiple variables with same name: Ctrl+D


# # List
# Create
my_list = [1, "Asim", True, 99, [1, 2, 3]]
# another_list=my_list[4]


# Sorting
numbers = [2, 5, 99, 3, 7, 8, 34]
print(numbers)
print(sorted(numbers, reverse=False))
print(numbers)
numbers.sort(reverse=False)
print(numbers)


# READ
# print(my_list[1])

# update
my_list.append("Kathmandu")
my_list.insert(2, "Nepal")
# print(my_list)
# my_list[2]="Nepal"
# my_list[4][1]=9
# print(my_list)

# Delete
# TO delete item from specific index
# my_list.pop(2)
# print(my_list)

# my_list.clear()
# print(my_list)


# del my_list
# print(my_list)

# # Dictionary

# # {key:value}
# # staff= {key:value}

# Create

staff = {
    "name": "Rishiraj",
    "is_married": True,
    "children": ['Jenny', 'Ruku'],
    "dob": {"year": 2000, 'month': 'Feb'}
}

# Read
# print(staff["name"])

# update
# staff["is_married"]=False
# print(staff["dob"]["year"])
# print(staff)


# Delete
# TO delete data of specific key
# staff.pop("is_married")
# staff.clear()
# del staff


# # [1,2,3]

# # staff1=["Rishi",True,2000]
# print(staff["name"])
# staff["age"]=33

# staff['age']

# print(staff)
# print(staff.items())
# # [(key,value),(key,value)]

# print(staff.values())
# #
# # print(staff.keys())

# staff.pop("children")
# print(staff)


# TUPLES
another = [1, 2, 3, 4, 1, 1]
another[3] = 99

my_tuple = (1, 2, 3, 4)
# my_tuple[3]=99

# SET

my_set = {1, 2, 3, 2, 3, 3, 3}
print(my_set)
