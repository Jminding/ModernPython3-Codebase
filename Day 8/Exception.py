age = 0
try:
    age = int(input("How old are you: "))
    print(age)
except ValueError:
    print("Invalid number.")