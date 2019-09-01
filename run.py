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
    Credential.delete_credential(Credential)

def display_credentials():
    '''
    Function for displaying credentials
    '''
    return Credential.display_credentials()

def main():

    print("Hello there welcome to password locker.Remember millions of passwords with one")
    print("Lets get started")
    print("-"*80)
    print("1. Create an Account")
    print("Please enter your username")
    user = input()
    print("Please enter your password")
    userpassword = input()
    save_users(create_user(user,userpassword))
    print(f"Congratulations {user} you have successfuly created an account!!")
    while True:
        print("press (1) to login into an account or (2) to exit the program")
        option = input()
        if option == "1":
            print("-"*10)
            print("2.Login to start managing your credentials")
            print("Username:")
            inputted_username = input()
            print("Password:")
            inputtedpassword = input()
            if inputtedpassword == userpassword and inputted_username == user:
                print(f"Hi {user} Welcome to your password portal")
                while True:
                    print("Use the following codes to navigate through your portal:\n ac - add credential  dc - delete credential  di - display credentials \n ex - exitportal")
                    print("Please Input your code:")
                    code = input()
                    if code == 'ac':
                        print("New Credential Creation")
                        print("-"*10)
                        userName = user
                        print("Please enter the platform you want to save the credentials for")
                        Site = input()
                        print("Please enter the user name for the site")
                        accountName = input()
                        print("Please enter the email used to create the account")
                        accountEmail = input()

                        print("Please enter the password to remember")
                        accountPassword =input()

                        save_credential(create_credentials(userName,Site,accountName,accountEmail,accountPassword))
                        print("\n")
                        print(f"New account credential created for {Site} account")
                        print("\n")

                    elif code == "di":
                        if display_credentials():
                            print("Here is a list of your credentials")
                            print('\n')

                            for credential in display_credentials():
                                print(f"Site:{credential.site}\n UserName:{credential.user_name}\n Password:{credential.account_password}")
                                print('\n')
                        else:
                            print('\n')
                            print("No credentials saved yet")
                            print('\n')

                    elif code == "dc":
                        print("Are you sure you want to delete this credentials y for Yes or n for No?")
                        answer = input()
                        if answer == "y":
                            # delete_credential(Credential)
                            print("Credentials deleted...")
                        else:
                            print("Whew that was close...")

                    elif code == "ex":
                        print("Thank you always a pleasure to be your storage option")     
                        break                     

                    else:
                        print("Please use the short codes provided")
                else:
                    print("please enter correct password or check whether your username matches your password")
        else:
            print("Welcome again")
            break       

if __name__ == "__main__":
    main()