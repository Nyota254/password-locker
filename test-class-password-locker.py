import unittest
from users import User
from credentials import Credential

class TestUsers(unittest.TestCase):
    '''
    Test class that defines test cases for the users

    Arg:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        This method stands for what is to to be loaded when the test class is run
        '''
        self.new_user = User("admin","admin")
        self.new_credentials = Credential("admin","twitter","admin","admin@admin.com","123456")

    def test_users_init(self):
        '''
        This class is to test whether a new instance was created
        '''
        # self.new_user = User("admin","admin")
        self.assertEqual(self.new_user.user_name,"admin")
        self.assertEqual(self.new_user.user_password,"admin")


        
