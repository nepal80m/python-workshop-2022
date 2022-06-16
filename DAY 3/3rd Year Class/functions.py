# int main(args){
#     statements
# }
# CTRL + D


# ARGS

def print_name(name, roll, *score):
    print(f"I am {name}. My roll is {roll}. My score is {score}")


print_name("Asim Nepal", 10, 1, 2, 34, 5)


def print_student(name, roll, math, science, english):
    print(
        f"I am {name}. My roll is {roll}. My scores are {math},{science}, {english}")


# Named parameters
print_student(name="Asim Nepal", roll=10, math=1, science=2, english=34)

# KWARGS


def print_student(name, roll, **scores):
    print(
        f"I am {name}. My roll is {roll}. My scores are {scores}")


# Named parameters
print_student(name="Asim Nepal", roll=10, math=1,
              science=2, english=34, jpt='jpt')
# (1, 2, 3,) *arg
# (math=1, science=2, english=3) **kwargs

# create a function that returns the max value from the given numbers


def find_max(*numbers):
    # numbers [1,2,3,5,6]
    max = numbers[0]
    for num in numbers:
        if num > max:
            max = num
    return max


print(find_max(-1, -2, -3, -5, -6))

# Assignment for day 3
# Take following staffs as input and perform required computations to create the final expected outcome.
# Input
staffs = [
    {"roll": 3, "name": "Your Name Here", "scores": [1, 2, 3]},
    {"roll": 10, "name": "Another Name Here", "scores": [4, 5, -6]},
    {"roll": 20, "name": "Yet Another Name Here", "scores": [-7, 0, -8, -9]},
]
# Expected Outcome
# staffs = [
#     {"roll": 3, "name": "Your Name Here", "max_score": 3, },
#     {"roll": 10, "name": "Another Name Here", "max_score": 5},
#     {"roll": 20, "name": "Yet Another Name Here", "max_score": 0},
# ]
