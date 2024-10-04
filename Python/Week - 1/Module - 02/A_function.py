# define
""" def sum(num1, num2):
    return num1 + num2


print(sum(1, 2)) """


# star args
def fun(*numbers):
    sum = 0
    for value in numbers:
        sum += value
    return sum


print(fun(1, 2, 3, 4, 5, 6))


def fun(num1, num2, *numbers):
    sum = 0
    for value in numbers:
        sum += value
    return sum


print(fun(1, 2, 3, 4, 5, 6))
