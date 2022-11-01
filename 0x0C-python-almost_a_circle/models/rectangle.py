#!/usr/bin/python3
"""the class Rectangle that inherits from Base"""

from models.base import Base


class Rectangle(Base):
    """the class Rectangle that inherits from Base]

    Args:
        Base ([cls]): [inherited class]
    """
    pass

    def __init__(self, width, height, x=0, y=0, id=None):
        """Call the super class with id - this super call
        with use the logic of the __init__ of the Base class
        Assign each argument width, height, x and y to the right attribute]

        Args:
            width ([int]): []
            height ([int]): []
            x (int, optional): []. Defaults to 0.
            y (int, optional): []. Defaults to 0.
            id ([id], optional): []. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        integer_validator(self, 'width', value)
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        integer_validator(self, 'height', value)
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        integer_validator_0(self, 'x', value)
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        integer_validator_0(self, 'y', value)
        self.__y = value

    def area(self):
        """
        Returns:
            [int] -- [area of Rectangle]
        """
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with
        the character # by taking care of x and y]
        """
        print('\n' * self.__y, end='')
        for height in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """
        Returns:
            [string] -- [the following rectangle description:
            [Rectangle] (<id>) <x>/<y> - <width>/<height>]
        """
        return '[Rectangle] ({}) {}/{} - {}/{}'\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """assigns a values argument to attributes"""
        tmp = ['id', 'width', 'height', 'x', 'y']
        if args:
            for pos, arg in enumerate(args):
                setattr(self, tmp[pos], arg)
        else:
            if len(kwargs) <= 0:
                return
            for key, value in kwargs.items():
                if key in tmp:
                    setattr(self, key, value)

    def to_dictionary(self):
        """create a dictionary with the representation of the rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }


def integer_validator(self, name, value):
    """method that validates value]

    Arguments:
        name {[string]}
        value {[int]}

    Raises:
        TypeError: [<name> must be an integer]
        ValueError: [<name> must be > 0]
    """
    if type(value) is not int:
        raise TypeError('{} must be an integer'.format(name))
    elif value <= 0:
        raise ValueError('{} must be > 0'.format(name))


def integer_validator_0(self, name, value):
    """method that validates value]

    Arguments:
        name {[string]}
        value {[int]}

    Raises:
        TypeError: [<name> must be an integer]
        ValueError: [<name> must be >= 0]
    """
    if type(value) is not int:
        raise TypeError('{} must be an integer'.format(name))
    elif value < 0:
        raise ValueError('{} must be >= 0'.format(name))
