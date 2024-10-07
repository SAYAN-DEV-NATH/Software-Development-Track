testcase = int(input())
while testcase != 0:
    n = int(input())
    numbers = input()
    numbersList = list(map(int, numbers.split()))
    mn = float("inf")
    for i in range(n):
        for j in range(i + 1, n):
            result = numbersList[i] + numbersList[j] + j - i
            mn = min(mn, result)
    print(mn)
    testcase -= 1
