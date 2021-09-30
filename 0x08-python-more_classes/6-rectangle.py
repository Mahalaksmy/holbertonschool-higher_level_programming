#!/usr/bin/python3
"""New class rectangle """


class Rectangle:
    """New class rectangle that defines a rectangle:"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize square with the size width and height"""

        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """New value for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting a new value for width"""

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """property  to retrieve it"""
        return self.__height

    @height.setter
    def height(self, value):
        """ New value for height"""

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Method that returns the rectangle area"""

        self.__area = self.__width * self.__height
        return self.__area

    def perimeter(self):
        """Method hat returns the rectangle perimeter"""

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            self.__perimeter = (self.__width + self.__height) * 2
            return self.__perimeter

    def __str__(self):
        """Method string of a rectangle"""

        print_s = ""
        if self.__width > 0 and self.__height > 0:
            for y in range(self.__height):
                for x in range(self.__width):
                    print_s = print_s + "#"
                print_s = print_s + "\n"
        return print_s[: -1]

    def __repr__(self):
        """“ A string representation of the rectangle"""

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Method for instance of Rectangle is deleted"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
