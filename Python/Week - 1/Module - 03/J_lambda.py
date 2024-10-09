# doubled = lambda num: num*2
# print(doubled(44))

# squared = lambda num : num **2
# print(squared(8))

# add = lambda a, b: a+b
# print(add(5,8))

actors = [
    {'Name': 'sabana', 'age': 65},
    {'Name': 'sabnoor', 'age': 45},
    {'Name': 'sabila noor', 'age': 30},
    {'Name': 'srabonti', 'age': 38},
    {'Name': 'shaon', 'age': 47},
]

juniors = filter(lambda actors:actors['age'] < 40, actors)
print(list(juniors))