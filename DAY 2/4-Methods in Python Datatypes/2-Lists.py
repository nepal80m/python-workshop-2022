# empty list
my_list = []

# list of integers
my_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# list with mixed data types

my_list_2 = [3, "Earth", True, 4.54]

# nested list
my_list_3 = [4, "Mars", ["Phobos", "Deimos"]]

# accessing list and list slicing
# print(my_list_1[0])
# print(my_list_2[-1])
# print(my_list_3[2])
# print(my_list_3[2][1])
# print(my_list_1[3:7])
# print(my_list_1[::-1])

# changing list
# my_list_1[0] = 0
# print(my_list_1)

# my_list_1[0:4] = [9,8,7,6]
# print(my_list_1)

# list methods
my_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

my_list_1.append(10)
print(my_list_1)

my_list_1.extend([11, 0, 13])
print(my_list_1)

print(my_list_1 + [1,2,3,4,55]) # alternate to extend

print(my_list_1.index(5))

print(sorted(my_list_1))
print(my_list_1)
my_list_1.sort(reverse=True)
print(my_list_1)

my_list_1.reverse()
print(my_list_1)

# insert, pop, count, remove, clear are some other methods that can be used in list

# Set - List with no repeating elements
my_set = {1, 2, 3, 3, 3}
print(my_set)

# Tuple - Immutable list
my_tuple = (1, 2, 3, 4, 3)
# my_tuple[0] = 2
print(my_tuple)

# string related to list
my_string = 'hello WORLD'
string_list = my_string.split()
print(string_list)
print(''.join(string_list))

print(list(my_string))

# Enter number of staffs: 2
# Staff 1:
# Name:
# Gender(M/F): 
# DOB (year):
# Is Married(yes/no):
# Staff 2:
# Name:
# Gender(M/F): 
# DOB (year):
# Is Married(yes/no):
# Staff number 1 is Rishi. He is 20 years old and unmarried.

# [
#     {'name':'Rishi', 'is_married':False,'age':20} 
#     {'name':'Raj', 'is_married':True,'age':25}
# ]

n=int(input("Enter the number of staffs:"))
staffs=[]
for i in range(n):
    print("Staff {i}:")
    name=input("Full Name:").title()
    gender=None
    while gender!='M' and gender!='F':
        gender=input("Gender(M/F)")
    year=input("DOB (year):")
    is_married=None
    while is_married!='yes' and is_married!='no':
        is_married=input("Is Married(yes/no)")
    is_married=True if is_married=='yes' else False
    age=2022-int(year)
    staffs.append({'name':name,'gender':gender,'is_married':is_married,'age':age})

for i,staff in enumerate(staffs):
    if staff['gender']=='M':
        pronoun='He'
    else:
        pronoun='She'
    if staff['is_married']:
        marital_status='married'
    else:
        marital_status='unmarried'
    first_name=name.split()[0]

    print(f"Staff number {i+1} is {first_name}. {pronoun} is {staff['age']} years old and {marital_status}.")
