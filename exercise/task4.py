def take_value():
    p = int(input("Enter p:"))
    t = int(input("Enter t:"))
    r = int(input("Enter r:"))
    return [p, t, r]  # list


def calculate():
    obj = take_value()
    p = obj[0]
    t = obj[1]
    r = obj[2]
    return p * t * r / 100


def display_value():
    print(calculate())


display_value()
