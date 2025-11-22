#Static attributes

# a static attribute(sometimes called a class attribute)
#is an attribute that belongs to the class itself, not to any
#specific instance of the class.

# there is only one copy of the static attribute in the memory

class User:
    user_count = 0

    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.user_count += 1

    def display_user(self):
        print(f"Username: {self.username}, Email: {self.email}")



user1 = User("john", "john@com")
user2 = User("busra", "busra@com")

print(User.user_count)