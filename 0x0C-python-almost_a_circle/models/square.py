#!/usr/bin/python3
"""The class Square
that inherits from Rectangle"""

from models.rectangle import  Rectangle

class Square(Rectangle):
    """Class Square that inherits
    from Rectangle"""
    
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square Class"""
        super().__init__(size, size, x, y, id)
        self.size = size
        
    def __str__(self):
        """ This a Method that returns
        [Square] (<id>) <x>/<y> - <size>"""
        
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width)

    @property
    def size(self):
        """getter of the self"""
        return self.width
    
    @size.setter
    def size(self,value):
        """Setter of the size"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value
    
    def update(self, *args, **kwargs):
        """Update the square: id, size, x, y."""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
        
        
        
        