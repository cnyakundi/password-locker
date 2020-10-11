import unittest

from userclass import User

from userclass import Credentials


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


class UserClassTest(unittest.TestCase):
    def setUp(self):
        '''
        method run before each test.  Gives the cutting guideline 
        '''
        self.new_account = Credentials("Twitter","cyprian","MyPassword")

    def tearDown(self):
        '''
        method run after each test to avoid errors just as explained in the LMS
        should come before the test. 
        '''
        Credentials.usercredential = []

    def test_init(self):
        '''
        test to check for proper initialization
        '''
        self.assertEqual(self.new_account.account_name,"Twitter")
        self.assertEqual(self.new_account.username,"cyprian")
        self.assertEqual(self.new_account.password,"MyPassword")

    def test_save_account(self):
        '''
        test method that checks if account has been saved
        '''
        self.new_account.save_account()
        self.assertEqual(len(Credentials.usercredential),1)

    def test_save_multiple(self):
        '''
        test method to check if user can add many accounts
        '''
        self.new_account.save_account()
        another_account = Credentials("Instagram", "Robert", "Alai1234")
        another_account.save_account()
        self.assertEqual(len(Credentials.usercredential),2) # We should have two of them
        
    def test_delete_account(self):
        '''
        test method to check if an account has been deleted
        '''
        self.new_account.save_account()
        another_account = Credentials("LinkedIn", "Sam", "Yayers")
        another_account.save_account()
        self.new_account.delete_account()
        self.assertEqual(len(Credentials.usercredential),1)
    
    def test_password_autogenerate(self):
    
        #test method to test auto generation of passwords
    
        self.new_account.save_account()
        another_account = Credentials("Blog", "Ger")
        another_account.save_account()

    def test_dislay_accounts(self):
        
        #test method for displaying  accounts
        
        self.new_account.save_account()
        another_account = Credentials("Gscroll","Edward", "Young-Tad")
        another_account.save_account()
        self.assertEqual(Credentials.display_accounts(),Credentials.usercredential)

    def test_search_accounts(self):
        '''
        test method to test search functionality
        '''
        self.new_account.save_account()
        another_account = Credentials("Facebook", "Kevin", "Stano1234")
        another_account.save_account()
        self.assertEqual(another_account,Credentials.search_accounts("Facebook"))

if __name__ == "__main__":
    unittest.main()