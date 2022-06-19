def find_division(a, b):
    try:
        ans = a/b
        print(f"{a}/{b} = {ans}")
    except ZeroDivisionError:
        print("You cannot pass second parameter as 0.")
    except TypeError:
        print("Handling something here")


find_division(4, 0)

# class MyError(Exception):
#     def __str__
