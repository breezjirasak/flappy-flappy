from vector import Vector


class Pipe:
    def __init__(self, corner, width, height):
        """ Initializes a Pipe object with corner, width, height attributes.

        :param corner: corner of border as vector
        :param width: width of border as int or float
        :param height: height of border as int or float
        """

        self.corner = corner
        self.width = width
        self.height = height

    def draw_pipe_up(self, painter):
        """ draw a upper pipe

        :param painter: Turtle
        """
        painter.width(2)
        painter.penup()
        painter.goto(self.corner.x, self.corner.y + 100)
        painter.pendown()
        painter.fillcolor("Green")
        painter.begin_fill()
        for side in range(2):
            painter.forward(self.width)
            painter.left(90)
            painter.forward(self.height)
            painter.left(90)
        painter.end_fill()

    def draw_pipe_down(self, painter):
        """ draw a lower pipe

        :param painter: Turtle
        """
        painter.width(2)
        painter.penup()
        painter.goto(self.corner.x, self.corner.y)
        painter.pendown()
        painter.fillcolor("Green")
        painter.begin_fill()
        for side in range(2):
            painter.forward(self.width)
            painter.right(90)
            painter.forward(self.height)
            painter.right(90)
        painter.end_fill()

    def update(self):
        """ update pipe at x-axis """
        self.corner.x -= 1.5

    @property
    def corner(self):
        """ Get the value as a private attribute """
        return self.__corner

    @corner.setter
    def corner(self, corner):
        """ Set the value of the private attribute """

        # corner must be a Vector
        if not isinstance(corner, Vector):
            raise TypeError('corner must be a Vector object')
        self.__corner = corner

    @property
    def width(self):
        """ Get the value as a private attribute """
        return self.__width

    @width.setter
    def width(self, width):
        """ Set the value of the private attribute """

        # width must be a number
        if not isinstance(width, (int, float)):
            raise TypeError('width must be a number')
        # width must be grater than zero
        elif width <= 0:
            raise ValueError('width must be greater than zero')
        self.__width = width

    @property
    def height(self):
        """ Get the value as a private attribute """
        return self.__height

    @height.setter
    def height(self, height):
        """ Set the value of the private attribute """

        # height must be a number
        if not isinstance(height, (int, float)):
            raise TypeError('height must be a number')
        # height must be greater than zero
        elif height <= 0:
            raise ValueError('height must be greater than zero')
        self.__height = height
