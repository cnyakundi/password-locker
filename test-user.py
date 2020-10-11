import unittest

from userclass import User


class UserTest(unittest.TestCase):
    def setUp(self):
        '''
        method must be run before each user test
        '''
        self.newuser = User("Cyprian", "IsItMe?") # Initializing new user object. We will test it

    def tearDown(self):
        '''
        This method called after each user test
        '''
        User.userlist = []

    def test_init(self):
        '''
        Performing first test method to check if user class is initialized correctly
        '''
        self.assertEqual(self.newuser.username,"Cyprian")
        self.assertEqual(self.newuser.password, "IsItMe")
        
    def test_save_user(self):
        '''
        test method to test if user has been saved into class list
        '''
        self.newuser.save_user()
        self.assertEqual(len(User.userlist),1) # Length of list as per lists concept 




