#Defining the user class that we will use to create the objects 
class User:
    userlist = []; #Userlist is an empty list. Will hold the data that we will append
    
    def  __init__(self, username, password):
        self.username= username
        self.password =password
        
    def save_user(self):
        #Saving the user object to the list we defined above
        User.userlist.append(self)
        
    