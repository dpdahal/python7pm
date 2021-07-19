nep = float(input("Enter nepali mark: "))
eng = float(input("Enter english mark: "))
math = float(input("Enter math mark: "))
sci = float(input("Enter science mark: "))
pop = float(input("Enter population mark: "))

total = nep + eng + math + sci + pop
percentage = total / 5

print("=============Result =============")
print(f"Total: {total}")
print(f"Percentage: {percentage}")

if percentage >= 35 and percentage <= 45:
    print("Third")
elif percentage >= 45 and percentage <= 60:
    print("Second")

elif percentage >= 60 and percentage <= 75:
    print("First")

elif percentage >= 75 and percentage <= 100:
    print("Top")
else:
    print("Just pass")
