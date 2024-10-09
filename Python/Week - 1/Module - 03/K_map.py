doubled = lambda a:a*2
numbers = [12, 56, 98, 78, 56, 12, 6, 98]

doubled_nums = map(doubled, numbers)
print(numbers)
print(list(doubled_nums))