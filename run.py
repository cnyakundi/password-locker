from userclass import User
from userclass import Credentials

def create_user(account_owner, account_key):
    
    #function to create a new user

    new_user = User(account_owner, account_key)
    return new_user


def save_user(data):

    #function to save a new user

    data.save_user()


def create_account(account, u_name, passwd):
    
    #function to create a new account
    
    new_account = Credentials(account, u_name, passwd)
    return new_account


def save_accounts(credentials):
    
    #function to save the new account
    
    credentials.save_account()


def delete_accounts(credentials):
    
    #function to delete an account
    
    credentials.delete_account()


def search_accounts(search):
    
    #function to find an account by account name
    
    return Credentials.search_accounts(search)


def generate_password():

    #function to generate a password
    
    random_password = Credentials.password_generate()
    return random_password


def display_account():
    
    #function to display all accounts saved

    return Credentials.display_accounts()



def main():

    print("\nHello and welcome!")
    print("\n 1. Create an account \n 2. Exit app")
    option = input()

    if option == '1':
        print("Enter your name")
        account_owner = input()
        if not account_owner:
            print("You must type something in")
        else:
            print("Enter a password")
            account_key = input()
            if not account_key:
                print("You must type something in")
            else:
                save_user(create_user(account_owner, account_key))
                print("-" * 10)
                print(f"{account_owner}, please enter your password again to login.")
                confirm = input()
                if confirm == account_key:
                    print("\n You are successfully logged in!")
                    while True:
                        print("-" * 10)
                        print(
                            "What would you like to do today? \n Use these short codes : \n \t\t aa - Add an account "
                            "using your own password \n \t\t ga - Generate a password for your new account \n \t\t da "
                            "- display saved accounts \n \t\t sa - Search for an account \n \t\t D - delete an "
                            " account \n \t\t ex - Exit")
                        short_code = input().lower()

                        
