balance = 3000  # global variable


def buy_things(item, price):
    global balance
    balance = balance - price
    print(f"balance after buying {item} : {balance}")


buy_things("sumglass", 1000)
