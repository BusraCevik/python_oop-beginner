#Accesing and Modifying Data:
#1. The traditional way: make the data private and use getter and setters:



class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

user1 = User("john", "john@com", "123")
