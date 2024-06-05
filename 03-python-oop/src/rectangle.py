# Class is like a blueprint for an object

class Rectangle:
    # constructor - function that builds the object
    def __init__(self, width, height):
        print('inside constructor')
        # To let other users know it's private and not meant to be altered write: self._width
        self.width = width # referring to setter of width
        self.height = height #referring to setter of height
        self.area = self.width * self.height
        
    # Getter and Setter functions
    
    def get_width(self):
        '''return the width'''
        print('inside getter')
        return self._width
    
    def set_width(self, new_width):
        '''update the existing width'''
        if isinstance(new_width, int) and new_width > 0: # type validation is not recommended here; Duck philosophy: if it looks and quakes like a duck, then it is a duck.
            self._width = new_width
        else:
            raise ValueError('width must be positive')
        
    # Property() creates attributes for the class
    
    width = property(get_width, set_width)
    
    # Property creates an abstract variable with two functions: getter and setter
    @property
    def height(self):
        '''Gets the height'''
        return self._height # Do not forget to add an underscore or it will be in an infinite loop
    
    @height.setter
    def height(self, new_height):
        '''Sets the new height'''
        self._height = new_height
        if isinstance(new_height, int) and new_height > 0:
            self._height = new_height
        else:
            raise ValueError('width must be positive')
    
    # methods are functions for class
    # get_area method is a function of class Rectangle
    def get_area(self):
        return self.width * self.height
    
    def get_circumference(self):
        return (2 * self.width) + (2 * self.height)
    
    def __repr__(self):
        return f'<Rectangle w:{self.width}, h:{self.height} a:{self.get_area()}'

# build a rectangle object
r1 = Rectangle(2, 3)
r2 = Rectangle(6, 9)

# DEBUGGING SECTION
print("type of r1: ", type(r1))
# print("width of r1: ", r1.width)
print("directly accessing the class attributes: ", r1.width, r1.height, r1.get_area(), r1.get_circumference())
# print("directly accessing the class attributes: ", r2.width, r2.height, r2.get_area(), r2.get_circumference())
print("r1 object:", r1)
print("r2 object:", r2)
# r1.set_width(99) #referring to width setter
r1.width = 99 # referring to width property, not width constructor attribute
print("get width of r1:", r1.get_width())
# print("getting all the attr and methods:", dir(r1))