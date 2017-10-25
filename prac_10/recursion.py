"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# TODO: 1. write down what you think the output of this will be,
# 3
# TODO: 2. use the debugger to step through and see what's actually happening
print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n > 0:
        print(n ** 2)
        do_something(n - 1)


# TODO: 3. write down what you think the output of this will be,
# 16
# 9
# 4
# 1
# TODO: 4. use the debugger to step through and see what's actually happening
do_something(4)


# TODO: 5. fix do_something() so that it works the way it probably should :)


# def how_many_bricks_in_pyramid(n):
#     number_of_bricks = 0
#     while n != 0:
#         number_of_bricks += n
#         n -= 1
#     return (number_of_bricks)


def how_many_bricks_in_pyramid(n):
    if n <= 0:
        return 0
    return n + how_many_bricks_in_pyramid(n-1)


bricks = how_many_bricks_in_pyramid(int(input("How many rows in the pyramid? ")))
print(bricks)