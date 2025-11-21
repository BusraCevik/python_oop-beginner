class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("Whoof whoof")

class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.contact_number = contact_number


owner1 = Owner("Busra", "dedbrreafgee", "12345678")
dog1 = Dog("Bruce", "Golden", owner1)
print(dog1.owner.address)

owner2 = Owner("Beyza", "dedfgfhtgbbe", "12378954245")
dog2 = Dog("Freya", "Grayhound", owner2)
print(dog2.name)