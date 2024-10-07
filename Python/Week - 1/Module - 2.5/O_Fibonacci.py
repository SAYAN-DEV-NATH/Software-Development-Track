n = int(input())
first = 0
second = 1

if n == 1:
    print(first)
elif n == 2:
    print(second)
else:
    n -= 2
    for i in range(n):
        ans = first + second
        first = second
        second = ans
    print(ans)
