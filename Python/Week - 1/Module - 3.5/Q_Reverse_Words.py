s = str(input())
flag = False
for word in s.split(" "):
    if flag:
        print(end=" ")
    flag = True
    for char in word[::-1]:
        print(char, end="")
