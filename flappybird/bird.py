from turtle import Screen
from vector import Vector


class Bird:
    def __init__(self, pos):
        """ Initializes a Bird object with pos attribute.

        :param pos: Vector
        """
        self.pos = pos

    def draw(self, painter):
        """ Draw a bird and update new x,y

        :param painter: Turtle
        """
        painter.penup()
        Screen().register_shape('bird.gif')
        painter.shape('bird.gif')
        painter.goto(self.pos.x, self.pos.y)

    def update(self):
        """ define y-axis """
        self.pos.y = 4

    @property
    def pos(self):
        """ Get pos value as a private attribute """
        return self.__pos

    @pos.setter
    def pos(self, pos):
        """ Set pos value of a private attribute """

        # pos must be a Vector
        if not isinstance(pos, Vector):
            raise TypeError('pos must be a Vector object')
        self.__pos = pos
