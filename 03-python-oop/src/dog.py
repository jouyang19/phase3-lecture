"""
Write a class that represents a dog. We should be able to:
- Access the dog's name, breed, and age
- Make the dog bark
- Print the dog as a string
"""

class Dog:
    def __init__(self, name="unknown", breed="unknown", age="unknown", is_good = False):
        self.name = name,
        self.breed = breed,
        self.age = age
        self.is_good = is_good
    def __repr__(self):
        return f'<Dog {self.name} {self.breed} {self.age} {self.is_good}>'
    
d1 = Dog('fido', 3)
print(d1)