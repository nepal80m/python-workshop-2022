# def name():
#     print("my name is mohammed")


# name()

# def fname(fnames):
#     print(fnames+" chauhaan")


# fname('risi')
# def details(name, roll, *score):
# print(f"I am {name}.MY roll is :{roll} and score{score}")


# details("sheikh", 21, 20, 1, 2, 3)

#list in functions


# def my_food(food):
#     for x in food:
#         print(x)


# fruits = ['apple', 'cherry', 'berry', 'risi', 'nischu','bipana']

# my_food(fruits)

def mul(x, y):
    return(x*y)


a = 2
b = 3
print(mul(3, 3))
print(mul(a, b))

# make a function that sums two values


def sum(*num):
    print(num)
    add = 0
    for i in num:
        add += i

    return(add)


print(sum(1, 2, 3, 4))


# assignment
Q1: Using * argument find a maximum value
in 5 numbers and return the value to called function
and print it
