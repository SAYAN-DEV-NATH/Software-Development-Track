""" def fullName(first, last):
    name = f"Full Name is: {first} {last}"
    return name


name = fullName("Ahlu", "kodu")
print(name)


def fullName(first, last):
    name = f"Full Name is: {first} {last}"
    return name


name = fullName(last="kodu", first="Ahlu")
print(name) """


# def famous(**kargs)
def famousName(first, last, **addition):
    print(addition["title"])
    for key, value in addition.items():
        print(f"{key} = {value}", end=" ")


famousName(first="Tahar", last="Ali", title="Hujur", addition="Shayokh")
