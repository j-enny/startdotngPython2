import string
import random
from validate_email import validate_email
from goto import with_goto

#function to create random password
def random_password(x,y):
    pass1 = x[0:2] + y[-2:]
    randompass = ''.join(random.choice(string.ascii_letters + string.digits) for n in range(5))
    generated_password = pass1.upper() + randompass
    return generated_password

#function to accept user preferred password
def input_password():
    upass = input("Enter your preferred password: ")
    return upass


#function to accept user input and convert to dictionary
@with_goto
def users():
    user_dict = {}
    firstName = input("FIRST NAME: ")
    lastName = input("LAST NAME: ")
    email = input("EMAIL: ")
    validmail = validate_email(email)

    while (validmail == False):
        print("Email is not valid!!!")
        email = input("Email: ")
        validmail = validate_email(email)
    else:
        valid_email = email


    password = random_password(firstName,lastName) #calling the password function
    print("Your generated password is:", password)

    user_choice = input("Do you want to keep it?(y/n)")

    if user_choice=='n':
        label .enterpassword
        upassword = input_password()
        if len(upassword) < 7 :
            print("password must not be less than 7 characters!!")
            goto .enterpassword
        else:
            confirm_password = input("Confirm Password: ")
            if confirm_password == upassword :
                confirmed_password = upassword
            else:
                print("password doesn't match!!")
                goto .enterpassword
    else:
        confirmed_password = password

    return email,firstName,lastName, confirmed_password


@with_goto
def main():
    users_DB = {}
    label .acceptNewUser
    allUsers = users()

    print(f'Dear {allUsers[1]} {allUsers[2]}, your account has been created with email {allUsers[0]} and password {allUsers[3]}')

    users_DB[allUsers[0]] = [allUsers[1], allUsers[2], allUsers[3]]

    moreUser = input("Do you have an existing account? (y/n)")

    if moreUser == 'y':
        existing = input("Email: ")
        if existing in users_DB:
            print("You are registered.")
            next = input("To register new employee, press new.")
            if next == 'new':
                goto .acceptNewUser
            else:
                exit()

        else:
            print("You do not have an existing account, please register.")
            goto .acceptNewUser
    else:
        goto .acceptNewUser


# Welcome the new employee to the platform
print("HELLO DEAR EMPLOYEE, YOU ARE WELCOME TO THE HNG TECH TEAM. \n IN A BID TO FULLY WELCOME  YOU TO THE TEAM YOU NEED TO CREATE AN ACCOUNT")
print("PLEASE INPUT YOUR DETAILS ACCORDINGLY")

main()