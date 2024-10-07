input_values = input()
a, b = map(int, input_values.split())

l = []
for i in range(a, b + 1):
    tmp = i
    flag = True
    while tmp != 0:
        r = tmp % 10
        tmp //= 10
        if r != 4 and r != 7:
            flag = False
            break
    if flag:
        l.append(i)

if len(l):
    for i in l:
        print(i, end=" ")
else:
    print("-1")
