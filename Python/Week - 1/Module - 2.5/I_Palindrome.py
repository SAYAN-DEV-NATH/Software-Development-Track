num = int(input())
sum = 0
tmp = num
while tmp != 0:
    rem = tmp % 10
    sum = sum * 10 + rem
    tmp //= 10
if sum == num:
    print(f"{sum}\nYES")
else:
    print(f"{sum}\nNO")
