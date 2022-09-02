import base64

# asks the user to create a master password that will be used later 
masterPassword = input("Create a master password: ")

# create function; the function that runs each time we want to create a new password
def create():
    username = input("Username: ")
    password = input("Password: ")

    file = open("info.txt", 'a') # creates a new file called info.txt for usersnames and passwords
    file.write(base64.b64encode(bytes(f"Username: {username}  Password: {password}\n", 'utf-8')).decode('utf-8')) # writes this in the info.txt file and creates a new line each time
    file.close() # closes the file after all the operations are done in order to prevent crashing

# view function; the function that runs each time we want to view our existing passwords
def view():
    
    userPasswordAttempt = input("What is the master password? ")
    
    if userPasswordAttempt == masterPassword:       # shows the user the text in the file if password inputed is correct
        file = open("info.txt", 'r')
        file_contents = base64.b64decode(file.read()).decode('utf-8')
        file.close()
        print(file_contents)
    else:                                           # ends the program if the password inputed is incorrect
        print("Wrong password. Access denied...")
        quit()

# delete function; the function that runs each time we want to delete our information
def delete():

    userPasswordAttempt = input("What is the master password? ")    

    if userPasswordAttempt == masterPassword:

        deleteConfirmation = input("Are you sure you want to delete(yes/no)? ").lower()     # asks for confirmation to delete information
        
        if deleteConfirmation == "yes":
            file = open("info.txt", 'w')
            file_contents = ""
            file.write(file_contents)
            file.close()
            print("Information deleted...")
        else:
            print("Deletion canceled...")
    
    else:                                           # ends the program if the password inputed is incorrect
        print("Wrong password. Access denied...")
        quit()
        

# a loop that continues forever until the user decides to quit
while True: 
    current_mode = input("Would you like to create a new password, view existing ones, or delete all passwords (view/create/delete, e to exit)? ").lower()

    if current_mode == "view":
        view()
    elif current_mode == "create":
        create()
    elif current_mode == "e":
        break
    elif current_mode == "delete":
        delete()
    else: 
        print("Not a valid mode. Try again...")
        continue