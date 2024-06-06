"""
Write a class that represents a dog. We should be able to:
- Access the dog's name, breed, and age
- Make the dog bark
- Print the dog as a string
"""

class Dog:
    all = []
    genus = 'canine'

    @classmethod
    def print_all_dogs(cls):
        print("print_all_dogs:")
        for dog in cls.all:
            print(dog)
    
    def __init__(self, name="unknown", age="unknown", breed="unknown", is_good = False):
        self.name = name,
        self.breed = breed,
        self.age = age
        self.is_good = is_good
        Dog.all.append(self)
        
    def __repr__(self):
        return f'<Dog {Dog.genus} {self.name} {self.breed} {self.age} {self.is_good}>'
    
    

d1 = Dog('fido', 6, 'pug', True)
d2 = Dog('Barley', 6, 'lab', True)
print("printing Dog.all:\n", Dog.all)
Dog.print_all_dogs()