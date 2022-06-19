x = 10


def my_func():
    x = 20

    def another_func():
        print(x)

    another_func()
    print(x)


my_func()
