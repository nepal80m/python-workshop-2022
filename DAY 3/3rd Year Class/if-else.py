
# if condition:
# statements
number = 0
# Determine if the number is even or odd
if number == 0:
    print("This is zero")
elif number > 0:
    print("This is a positive number")
else:
    print("This is a negative number")


is_vaccinated = True
age = 18
# if vaccinated and above 18 can enter
# below 18 reject
# if above 18 but not vaccinated....get vaccinated..

if age > 18 and is_vaccinated:
    print("welcome to the club")
elif not is_vaccinated:
    print("Go corona Go!!")
else:
    print("You are too young for the bar.")

#     # IN C/C++
# if(condition){
#     statement
# }

# In python there is no curly braces {} so note the indentation.

# Ternary if else
# condition?value1:value2
age = 53
category = 'old' if age > 60 else "young dumb"
