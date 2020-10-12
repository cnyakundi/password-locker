
import pyperclip
import random





#Defining the user class that we will use to create the objects 
class User:
    
    userlist = []; #Userlist is an empty list. Will hold the data that we will append
    
    def  __init__(self, username, password):
        self.username= username
        self.password =password
        
    def save_user(self):
        #Saving the user object to the list we defined above
        User.userlist.append(self)

# Credential Class that will be used to create account objects
class Credentials:

    usercredential = []  # creating an empty list of accounts

    def __init__(self, account_name, username, password=None): #Initializing 
    
        self.account_name = account_name 
        self.username = username
        self.password = password if password else Credentials.password_generate() 

    
    
    # Defining a method  that we will use to to save account object
    def save_account(self): 
        
        Credentials.usercredential.append(self)


    #Defining a methos that we will use to delete account details 
    def delete_account(self):
    
        Credentials.usercredential.remove(self)

    
    #Defining a class methose that will be used to generate a random password. 
    @classmethod
    def password_generate(cls):
        
        password_length = 8
        #Here we try to use the Regex logic to generate a random password. Ww imported random above
        possible_characters = "@abcdefghijklmnopqrstuvwxyz-1234567890&ABCDEFGHIJKLMNOPQRSTUVWXYZ!" 
        random_character = [random.choice(possible_characters) for i in range(password_length)]
        auto_password = "".join(random_character)
        return auto_password


    # We define class method that will be used to display all our contacts
    @classmethod
    def display_accounts(cls):
        return cls.usercredential
    
    
    
    # We define a class method to search for an account by account name
    @classmethod
    def search_accounts(cls, search):
        
        for acc in cls.usercredential:
            if acc.account_name == search:
                return acc



    #Defining  a  class method that will copy contacts courtesy of perperclip 
    @classmethod
    def copy_password(cls):
        
        for acc in cls.usercredential:
            pyperclip.copy(acc.password)
            pyperclip.paste()
        
