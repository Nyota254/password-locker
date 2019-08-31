#!/usr/bin/env python3.6

from users import User
from credentials import Credential

def create_user(user,userpassword):
    '''
    Function for creating users and their passwords
    '''
    new_user = User(user,userpassword)
    return new_user

def save_users(User):
    '''
    Function for saving users
    '''
    User.save_user()

def create_credentials(userName,Site,accountName,accountEmail,accountPassword):
    '''
    Function for creating new credential 
    '''
    new_credential = Credential(userName,Site,accountName,accountEmail,accountPassword)
    return new_credential

def save_credential(Credential):
    '''
    Function for saving credential
    '''
    Credential.save_credentials()

def delete_credential(Credential):
    '''
    Function for deleting credentials
    '''
    Credential.delete_credentials()

def display_credentials():
    '''
    Function for displaying credentials
    '''
    return Credential.display_credentials()

def main():


    print("Hello there welcome to password locker.Remember millions of passwords with one")
    print("Lets get started")
    print("1. Create an Account")
    print("Please enter your username")
    user = input()
    print("Please enter your password")
    userpassword = input()
    save_users(create_user(user,userpassword))
    print(f"Congratulations {user} you have successfuly created an account!!")
    while True:
        print("2.Login to start managing your credentials")
        print("Username:")
        inputted_username = input()
        print("Password:")
        inputtedpassword = input()
        if inputtedpassword == userpassword and inputted_username == user:
            print(f"Hi {user} Welcome to your password portal")
            print("Use the following codes to navigate through your portal")
            break
        else:
            print("please enter correct password or check whether your username matches your password")


if __name__ == "__main__":
    main()