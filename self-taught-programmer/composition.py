# composition: storing an object as a variable in another object

class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner


class Person:
    def __init__(self, name):
        self.name = name


george = Person("George Jeffries")
buddy = Dog("Buddy", "Mastiff", george)

print(buddy.owner.name)
