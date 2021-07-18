# x = 10
#
# print(dir(x))
# print(type(x))
# name = 'ram'
# print(dir(name))

# Numeric: int,float,complex


# int, float, string, boolean,none
#  list,tuple, set, dic

# a = 1.98765787687
# print(type(a))
# print("%.2f" % a)
#
# print("".format())
# print(f"")
# a = 10j
# print(type(a))
# print(dir(a))
# print(type(a))

# x = "python"
# y = 123
# print(x + " " + str(y))
# print("{} {}".format(x, y))
# print(f"{x} {y}")
# type casting
# print(x.upper())
# print(type(x))
# print(dir(x))

# print(x)

# print(type(x))

# x = input("Enter any number: ")
# print(type(x))
# y = input("Enter any number: ")
# print(int(x) + int(y))

# x, y = input("Enter x, y").split(",")
# print(x)
# print(y)

# x = 20
# y = 30

# x, y, z = 20, 30, 40
# print(x)
# print(y)
# print(z)

# print(2 < 3)

# age = None
# print(age)

# x = 1323

# list
# like c: array
# data = ["ram", 1234, 34.56, 'sita']
# print(data[1])

# data = ["kalpan", "sophia", 'madan', 'xyz']
# print(data[1])

# students = [
#     ["ram", 1234, 34.56, 'sita'],
#     ["hari", 67, 65, 'gita'],
#     ["kalpan", "sophia", 'madan', 'xyz'],
#     ["laxmi", ["gopal", ["mobile"]], 'abc']
# ]
#
# print(students[3][1][1][0])

# print(students[2][1])


# data = ["ram", 'sita']
# data.append("abc")
# print(data)
# print(type(data))
# print(dir(data))
# print(data)
# data[0] = "hari"
# print(data)

# data = ['ram', 'sita', 'gita']
# res = data[0]
# print(res[0])

# print(data[0][:-1])

# Tuple


# data = ("ram", 'sita', 'gita', 'sophia', 12, 356)
# print(data[0])
# data[0] = "abc"

# print(type(data))

# SET - unique
# {} empty: disc - {'ram','sita'}


# data = {'ram', 'sita', 'gita', 'sophia', 'ram', 123, 456, 123}

# data1 = {"name": 'ram', 'gae': 20}
# print(data1)
# print(dir(data))
# print(data)
# print(type(data))

users = [
    {"id": 1, "name": "Sophia", "address": "Kathmandu"},
    {"id": 2, "name": "Hari", "address": [
        {"tmp": "KTM"},
        {"pre": "LTP"}
    ]
     }
]
print(users[1]['address'][0]['tmp'])

# print(users[1]['name'])

# print(users['name'])
