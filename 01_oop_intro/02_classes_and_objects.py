#Accesing and Modifying Data:
#1. The traditional way: make the data private and use getter and setters:


'''
class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email
user1 = User("john", "john@com", "123")
print(user1.get_email())

'''



# 2. Properties

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    @property
    def email(self):
        print("Email accessed")
        return self._email

    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email


user1 = User("john", "john@com", "123")
user1.email = "this is not an email"
print(user1.email)

