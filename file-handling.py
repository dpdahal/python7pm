# CRUD
# C- create, R- read, U- Update, D- Delete
# model: w: write, a: append, a+: both read and write
# handle = open("record.txt", "w")
# handle.write("we are learning file handling...")
# handle.close()
# print(dir(handle))

# fs = open('record.txt', 'r')
# print(fs.readline())
# print(fs.readlines())
# print(fs.read())


# import os
#
# os.remove('record.txt')
# import os
#
# if os.path.exists('record.txt'):
#     os.remove('record.txt')
# else:
#     print("file not found")


# x = int(input("Enter any x: "))
# y = int(input("Enter any y: "))
#
# fs = open('record.txt', 'a')
# sum = f"Total: {x + y}"
# fs.write(sum)
# fs.write("\n")
# fs.close()

def register():
    pass


def login():
    pass


qn = input("Do you have an account y/n")

if qn == 'y':
    login()

else:
    register()
