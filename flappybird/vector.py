class Vector:
    def __init__(self, x, y):
        """ Initializes Vector object with x and y attribute.

        :param x: x-axis as int or float
        :param y: y-axis as int or float
        """
        self.x = x
        self.y = y

    @property
    def x(self):
        """ Get x value as a private attribute """
        return self.__x

    @x.setter
    def x(self, x):
        """ Set x value of a private attribute """

        # x must be a number
        if not isinstance(x, (int, float)):
            raise TypeError('x must be a number')
        self.__x = x

    @property
    def y(self):
        """ Get y value as a private attribute """
        return self.__y

    @y.setter
    def y(self, y):
        """ Set y value of a private attribute """

        # y must be a number
        if not isinstance(y, (int, float)):
            raise TypeError('y must be a number')
        self.__y = y
