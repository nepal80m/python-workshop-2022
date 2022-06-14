my_string = 'hello WORLD'

print(my_string * 3)

# String Slicing
print(my_string[0])
print(my_string[-1])
print(my_string[0:5])
print(my_string[6:-1])
print(my_string[0:8:2])
print(my_string[::-1])


phrase = "Gotta catch 'em all!"
# Output: hatch 'em all
print('h' + phrase[7:-1])

# String Methods
# print(f"Upper string : {my_string.upper()}")
# print(f"Lower string : {my_string.lower()}")
# print(f"Titled string : {my_string.title()}")
# print(f"Capitalized string : {my_string.capitalize()}")

# print(f"String length : {len(my_string)}")
print(my_string.find('ell'))
print(my_string.replace('ell', 'lle'))
