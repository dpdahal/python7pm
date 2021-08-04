import os.path
import getpass

if not os.path.exists('db.txt'):
    fs = open('db.txt', 'w')
    fs.close()


def register():
    print("=======New user register =============")
    username = input("Enter username: ")
    if username in open('db.txt').read():
        print("Username already exists")
        exit()
    password = getpass.getpass("Enter password: ")
    confirm_password = getpass.getpass("Enter confirm password: ")
    if password != confirm_password:
        print("password not match")
        exit()

    handle = open('db.txt', 'a')
    handle.write(username)
    handle.write(" ")
    handle.write(password)
    handle.write("\n")
    handle.close()
    print("User was successfully created")
    exit()


def login():
    print("=======Login user =============")
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    get_record = open('db.txt', 'r').readlines()
    user_data = []
    for user in get_record:
        user_data.append(user.split())

    total_user = len(user_data)
    increment = 0
    login_success = False
    while increment < total_user:
        uname = user_data[increment][0]
        u_pass = user_data[increment][1]
        if username == uname and password == u_pass:
            login_success = True

        increment += 1

    if login_success == True:
        print(f"Welcome {username}")
    else:
        print("Username & password not match")


question = input("Do you have an account? y/n: ")

if question == 'y':
    login()
else:
    register()
