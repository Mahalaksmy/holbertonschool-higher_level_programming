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
        
        
        