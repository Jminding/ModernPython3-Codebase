# Custom input function

def my_input(prompt):
    with open(1, 'w') as stdout:
        stdout.write(prompt)
    return open(0).readline().split()[0]
name = my_input("What's your name? ")
print(f"Hello, {name}!")