#!/usr/bin/python3
"""summary]

    Returns:
        [type]: [description]
    """

from models.rectangle import Rectangle


class Square(Rectangle):
    """the class Square that inherits from Rectangle]

    Args:
        Rectangle ([cls]): [inherited class]
    """
    pass

    def __init__(self, size, x=0, y=0, id=None):
        """
        Args:
            size ([int]): [size of square]
            x (int, optional): []. Defaults to 0.
            y (int, optional): []. Defaults to 0.
            id ([id], optional): []. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns:
            [string] -- [the following square description:
            [Square] (<id>) <x>/<y> - <size>]
        """
        return '[Square] ({}) {}/{} - {}'\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns a values argument to attributes"""
        tmp = ['id', 'size', 'x', 'y']
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
        """return dictionary"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
