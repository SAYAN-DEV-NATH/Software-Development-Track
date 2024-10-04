# define
""" def sum(num1, num2):
    return num1 + num2


print(sum(1, 2)) """


""" def sum(num1, num2, num3=0, num4=0, num5=0):
    result = num1 + num2 + num3 + num4 + num5
    return result


print(sum(1, 2)) """


def fun(num1, num2):
    sum = num1 + num2
    mult = num2 * num1
    mod = num1 % num2
    # return sum, mult, mod  # tripe
    return [sum, mult, mod]  # list


print(fun(55, 50))
