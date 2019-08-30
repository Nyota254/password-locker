import random
import string

class Credential:
    '''
    class for storing user credentials in the application
    '''
    Credentials = []
    def __init__(self,user_name,site,account_name,account_email,account_password):
        '''
        method for initialising account information 
        '''
        self.user_name = user_name
        self.site = site
        self.account_name = account_name
        self.account_email = account_email
        self.account_password = account_password

    def save_credentials(self):
        '''
        Method for saving user credentials i.e data
        '''
        Credential.Credentials.append(self)

    def password_generator(self):
        '''
        Method for random password generation
        '''
        
        password_characters = string.ascii_letters + string.digits + string.punctuation
        random_password = ''.join(random.choice(password_characters)for i in range(10))
        print(str(random_password))
        return str(random_password)

    def delete_credential(self):
        '''
        Method for deleting credentials
        '''
        Credential.Credentials.remove(self)

    
