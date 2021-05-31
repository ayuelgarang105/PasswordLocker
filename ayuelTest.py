import unittest  
from ayuelTest import User  
from ayuelTest import Credentials  
import pyperclip

class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        method to run each test
        '''
        self.user = User("Ayuel", "2021")
    def test_init(self):
        '''
        check proper user initialization
        '''
        self.assertEqual(self.user.user_name, "Ayuel")
        self.assertEqual(self.user.password, "2021")
    def tearDown(self):
        '''
        method to clean up after each test
        '''
        User.userList = []
    def test_save_multiple_users(self):
        '''
        method to test multiple saved users
        '''
        self.user.saveUser()
        test_user = User("Ayuel", "2021")  
        test_user.saveUser()
        self.assertEqual(len(User.userList), 2)
    def test_delete_user(self):
        """
        delete users
        """
        self.user.saveUser()
        test_user = User("Ayuel", "2021") 
        test_user.saveUser()
        self.user.deleteUser()
        self.assertEqual(len(User.userList), 1)
    def test_display_users(self):
        """
        method to test if users are correctly displayed
        """
        self.assertEqual(User.displayUser(), User.userList)
class TestCredentials (unittest.TestCase):
    def setUp(self):
        """
        define the constructor
        """
        self.cred = Credentials("Facebook", "Ayuel", "2021A")
    def tearDown(self,parameter_list):
        """
        clear up during each test
        """
        pass
    def test_init(self):
        """
        make sure the constructor is well initialized
        """
        self.assertEqual(self.cred.accountName, "Facebook")
        self.assertEqual(self.cred.accountUsername, "Ayuel")
        self.assertEqual(self.cred.accountPassword, "2021")
    def test_save_multiples_cred(self):
        """
        test for multiple credentials
        """
        self.cred.saveCredential()
        test_cred = Credentials("Facebook", "Ayuel", 2021)  
        test_cred.saveCredential()
        self.assertEqual(len(Credentials.credentials), 3)
    def test_delete(self):
        """
        test if the credential can be deleted
        """
        self.cred.saveCredential()
        test_cred = Credentials("Facebook", "Ayuel", 2021)  
        test_cred.saveCredential()
        self.cred.deleteCredential()
        self.assertEqual(len(Credentials.credentials), 1)
    def test_search(self):
        """
        search a credential
        """
        self.cred.searchCredential()
        test_cred = Credentials("Facebook", "Ayuel", 2021)  
        test_cred.searchCredential()
        found = Credentials.searchCredential("Facebook")
        self.assertEqual(found.accountName, test_cred.accountName)
    def test_display(self):
        """
        method to test if credentials can be displayed
        """
        self.assertEqual(Credentials.displayCredential(), Credentials.credentials)
if __name__ == "__main__":
    unittest.main()