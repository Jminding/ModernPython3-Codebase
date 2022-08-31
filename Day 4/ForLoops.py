for i in range(10):
    username = input("Username: ")
    pwd = input("Password: ")
    if username != "jayisded":
        print("Access not gained.")
        continue
    if pwd != "dee":
        print("Access not gained.")
    else:
        print("Access gained.")