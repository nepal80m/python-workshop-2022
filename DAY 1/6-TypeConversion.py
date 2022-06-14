# Question: Input your birth year and print your age based on the input.
dateOfBirth = input("What is your DOB (year)? : ")
currentYear = 2022


# age = currentYear - dateOfBirth

# print(age)

# print(type(dateOfBirth))
# print(type(currentYear))

age = currentYear - int(dateOfBirth)
print("Your age is ", age)
print("Your age is "+ str(age))
