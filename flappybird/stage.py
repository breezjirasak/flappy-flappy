import copy
from turtle import Turtle, Screen


class Stage:
    def __init__(self, bird, data):
        """  Initialize a Stage object with pipe, bird, data, painter, angry_bird, screen attribute

        :param bird: Bird object
        :param data: DATA object
        """

        # a list of object that keep Pipe object
        self.pipe = []
        self.bird = bird
        self.data = data
        self.painter = Turtle()
        self.angry_bird = Turtle()
        self.screen = Screen()

    def init_screen(self):
        """ Create a screen """
        self.screen.setup(550, 450)
        self.screen.title('Flappy Flappy')
        self.screen.bgcolor('Orange')
        # turn off animations of turtle
        self.screen.tracer(0)

    def add_pipe(self, pipe):
        """  Send Pipe object to a list

        :param pipe: Pipe object
        """
        pipe_ = copy.deepcopy(pipe)
        self.pipe.append(pipe_)

    def update_pipe(self):
        """ Updates each Pipe object in list """
        for i in self.pipe:
            i.update()

    def render_pipe(self):
        """ Draw a pipe in the screen """
        self.painter.clear()
        for i in self.pipe:
            i.draw_pipe_up(painter=self.painter)
            i.draw_pipe_down(painter=self.painter)
        self.screen.update()

    def render_bird(self):
        """ Draw a bird in the screen """
        self.painter.clear()
        self.bird.draw(painter=self.angry_bird)

    def press_bird(self):
        """ press space bar to set y position """
        self.screen.listen()
        self.screen.onkey(self.bird.update, 'space')

    def jump(self, gravity):
        """ update y position of bird wth gravity """
        self.bird.pos.y += gravity
        y = self.angry_bird.ycor()
        y += self.bird.pos.y
        self.angry_bird.sety(y)
        print(f'Bird at y position = {int(y)}.')

    def check_crash(self):
        """ to check the bird that crash the pipe or not """
        for i in range(len(self.pipe)):
            if self.bird.pos.x > self.pipe[i].corner.x + 65:
                self.data.score += 1
                self.pipe.pop(i)
            elif self.bird.pos.x + 20 > self.pipe[i].corner.x and (
                    self.angry_bird.ycor() - 17 < self.pipe[i].corner.y or self.angry_bird.ycor() + 16 > self.pipe[
                i].corner.y + 100):
                return True
            else:
                return False

    def text(self, text, size, y):
        """ to display text in the screen with turtle

        :param text: str
        :param size: int
        :param y: position at y-axis as int or float
        """
        draw = Turtle()
        font_size = size
        draw.penup()
        draw.sety(y)
        draw.pendown()
        draw.color('White')
        draw.write(text, font=("Arial", font_size, "normal"), align='center')
        draw.hideturtle()

    def score(self):
        """ to display score in the screen """
        score = self.data.score
        draw = Turtle()
        draw.penup()
        draw.goto(215, 170)
        draw.pendown()
        draw.color('White')
        draw.write(score, font=("Arial", 40, "normal"))
        draw.hideturtle()
        draw.clear()
        print(f'Score = {score}')

