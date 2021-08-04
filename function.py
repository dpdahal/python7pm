# A function is a block of code that only runes when it is called
# Types of function:
# 1. Inbuilt function: print(), len(),int()
# 2. User define function or custom function

# define function
# def course():
#     # function body part
#     print("Online python class")
#
#
# # calling
# course()

# def add(x, y):
#     print(x + y)
#
#
# add(20,20,40)

#
# def course(name):
#     print(f"Online {name} class")
#
#
# course('python')
# course('java')
# course('web development')

# def introduction(name, age=10):
#     print(name, age)
#
#
# introduction('ram', 20)
#
# introduction('sita',40)

# def add(x, y):
#     print(x + y)
#
#
# add(20, 20)

# function return value


# def add(x, y):
#     # print(x + y)
#     return x + y
#
#
# a = add(30, 20)
# print(a)  # None
# print(add(10, 20))


# def add_sub(x, y):
#     add = x + y
#     sub = x - y
#     return [add, sub]
#
#
# print(add_sub(20, 10))


# def test():
#     print("hello test")
#
#
# def get():
#     test()
#
#
# get()


# def take_value():
#     pass
#
#
# def calculate():
#     pass
#
#
# def display_value():
#     pass

# def my_rep(data, times):
#     pass
#
#
# my_rep('python', 200)


# function scope

# global
# local

# x = 10
#
#
# def test():
#     global x
#     x = x + 20
#     print(x)
#
#
# test()

#
# def students(names):
#     print(names)
#
#
# students(['sita', 'ram', 'hari'])

# * args: array arguments
# ** kwrgs: keyword arguments

# def students(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# students('sita', 'ram', name='hari', age=20, phone=98798)

# def test():
#     """
#     this is test
#     function
#     """
#     return "Hello"
#
#
# print(test.__doc__)
# print(test.__name__)


# add = lambda x, y: x + y
#
# print(add(20, 30))

# def introduction():
#     def get_function(name):
#         return f"I am {name} function"
#
#     return get_function
#
#
# # print(introduction()())
# obj = introduction()
#
# print(obj('ram'))


# recursive

# 5 = 120

#
# def recursive(n):
#     if n == 1:
#         return 1
#     else:
#         return n * recursive(n - 1)
#
#
# print(recursive(5))

# 5-1 =4
# 4-1 =3
# 3-1=2
# 2-1 =1

#
# import calculator
#
# print(calculator.add(20, 40))
# print(calculator.sub(40, 50))

# * all
from calculator import add
from database import add as test

print(add(10, 20))
print(test())

# from calculator import *
#
# print(add(30, 60))
# print(sub(5, 8))
