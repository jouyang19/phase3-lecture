"""
Write a class that represents a dog. We should be able to:
- Access the dog's name, breed, and age
- Make the dog bark
- Print the dog as a string
"""

class Pet:
    def __init__(self, name="unknown", age="unknown", sound='hello'):
        self.name = name,
        self.age = age
        self.sound = sound
        
    def say_hi(self):
        print(f'{self.name} says {self.sound}')
        
    def __repr__(self):
        return f'<Pet {self.name} {self.age}>'
    

class Dog(Pet):
    def __init__(self, name="unknown", age="unknown", breed="unknown"):
        super().__init__(name, age, sound='bark') # Calls the parent constructor
        self.breed = breed
    def __repr__(self):
        return f'<Dog {self.name} {self.age} {self.breed}>'
    
class Cat(Pet):
    def __init__(self, name="unknown", age="unknown", breed="american tabby"):
        super().__init__(name, age, sound="meow")
    def __repr__(self):
        return f'<Cat {self.name} {self.age}>'
    
d1 = Dog('fido', 3, "pug")
print(d1)
d1.say_hi()
c1 = Cat('Momo', 5, "tabby")
c1.say_hi()
print(c1)

pets = [
    Dog('fido', 3, "pug"),
    Cat('Momo', 5, "tabby"),
    Cat('Coco', 6, "tabby")
]

for pet in pets:
    pet.say_hi()

