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