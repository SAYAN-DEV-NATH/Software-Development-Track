nums = input()
a, b = map(int, nums.split())
s = str(input())

if s[a] == "-":
    flag1 = True
    flag2 = True
    l = len(s)
    for i in range(a):
        if "0" <= s[i] <= "9":
            continue
        else:
            flag1 = False
            break
    for i in range(a + 1, l):
        if "0" <= s[i] <= "9":
            continue
        else:
            flag2 = False
            break
    if flag1 and flag2:
        print("Yes")
    else:
        print("No")
else:
    print("No")
