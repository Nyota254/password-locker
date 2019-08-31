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

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.Credentials = []            
    
    def test_users_init(self):
        '''
        This class is to test whether a new instance was created
        '''
        # self.new_user = User("admin","admin")
        self.assertEqual(self.new_user.user_name,"admin")
        self.assertEqual(self.new_user.user_password,"admin")

    def test_save_user(self):
        '''
        This is a test to see whether the user can save their user name
        '''
        
        self.new_user.save_user()
        self.assertEqual(len(User.user_details),1)

###########################################################################################
#CREDENTIALS TESTS BEGIN HERE
###########################################################################################

    def test_credentials_init(self):
        '''
        This test tests if the class credentials instanciates the data
        '''
        self.assertEqual(self.new_credentials.user_name,"admin")
        self.assertEqual(self.new_credentials.site,"twitter")
        self.assertEqual(self.new_credentials.account_name,"admin")
        self.assertEqual(self.new_credentials.account_email,"admin@admin.com")
        self.assertEqual(self.new_credentials.account_password,"123456")
    def test_save_credentials(self):
        '''
        This test is to test if we can save the credentials
        '''

        self.new_credentials.save_credentials()

        self.assertEqual(len(Credential.Credentials),1)

    # def test_password_randomiser(self):
    #     '''
    #     test for random password generator
    #     '''
    #     #self.password_characters = string.ascii_letters + string.digits + string.punctuation
    #     self.new_credentials2 = Credential("admin2","twitter2","admin2","admin2@admin.com",password_generator())
    #     self.new_credentials2.save_credentials()
    #     self.assertEqual(new_credentials2.account_password,0)

    def test_delete_credential(self):
        '''
        test for deleting of credentials
        '''
        self.new_credentials.save_credentials()
        self.new_credentials2 = Credential("admin2","twitter2","admin2","admin2@admin.com","1234567")
        self.new_credentials2.save_credentials()

        self.new_credentials.delete_credential()
        self.assertEqual(len(Credential.Credentials),1)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credential.display_credentials(),Credential.Credentials)


if __name__ == "__main__":
    unittest.main()

        
