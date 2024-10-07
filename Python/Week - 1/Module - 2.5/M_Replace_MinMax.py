n = int(input())
numbers = input()
numbersList = list(map(int, numbers.split()))

mn = min(numbersList)
mx = max(numbersList)

mnIndex = numbersList.index(mn)
mxIndex = numbersList.index(mx)

numbersList[mnIndex], numbersList[mxIndex] = numbersList[mxIndex], numbersList[mnIndex]

for i in numbersList:
    print(f"{i}", end=" ")
