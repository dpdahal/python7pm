num = int(input("Enter number of student: "))

increment = 1

students_mark = []

while increment <= num:
    print(f"=======Student {increment}======")
    for x in range(1):
        nep = float(input("Enter nepali mark: "))
        eng = float(input("Enter english mark: "))
        math = float(input("Enter math mark: "))
        sci = float(input("Enter science mark: "))
        pop = float(input("Enter population mark: "))
        s_mk = [nep, eng, math, sci, pop]
        students_mark.append(s_mk)

    increment += 1

get_mark = []
for smk in students_mark:
    tot = 0
    for x in smk:
        tot += x

    get_mark.append(tot)

a = 0
for student in get_mark:
    a += 1
    percentage = student / 5
    division = ''
    if percentage > 35 and percentage <= 45:
        division += "Third"
    elif percentage > 45 and percentage <= 60:
        division += "Second"
    elif percentage > 60 and percentage <= 75:
        division += "First"
    elif percentage > 75 and percentage <= 100:
        division += "Top"
    else:
        division += "Pass"

    print(f"=========Student Result {a}==========")
    print(f"Total: {student} Percentage: {percentage} Division: {division}")
    print("=====================")


