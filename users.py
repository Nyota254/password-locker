

class User:
    '''
    Class for storing user information such as name and password
    '''
    user_details = []
    def __init__(self,user_name,user_password):
        '''
        Initialise method that helps us define properties for our object
        Arg:
            user_name: new Users user_name
            user_password:new Users user_password
        '''
        self.user_name = user_name
        self.user_password = user_password
    
    def save_user(self):
        '''
        method to save user into the users list
        '''
        User.user_details.append(self)