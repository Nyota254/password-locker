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