from turtle import Screen
from bird import Bird
from vector import Vector
from pipe import Pipe
from data import DATA
from stage import Stage
import random

bird = Bird(Vector(-220, 0))
stage = Stage(bird, DATA())
num_pipe = 100
width_pipe = 50
height_pipe = 400
gravity = -0.2

for i in range(num_pipe):
    # random position of gap
    y_gap = random.randint(-200, 130)

    # create Pipe object
    rectangle = Pipe(Vector(0 + i * 220, y_gap), width_pipe, height_pipe)
    stage.add_pipe(rectangle)

# create the screen
stage.init_screen()
# input name
name = Screen().textinput(title='LOGIN', prompt='TYPE YOUR NAME')

# if name already input then game will start
if name:
    data = DATA(name=name)
    stage.text("PRESS SPACE BAR TO JUMP", 10, -200)
    stage.press_bird()
    stage.render_bird()
    while True:
        stage.jump(gravity)
        stage.render_pipe()
        stage.update_pipe()
        stage.score()
        if stage.check_crash():
            stage.text("GAME OVER", 40, -5)
            stage.text(f"YOUR SCORE: {stage.data.score}", 30, -45)

            # keep score in data
            data.score = stage.data.score
            data.insert()

            # create list of dict
            data.score_name()

            # display high score
            new_data = [int(i['score']) for i in data.list_score]
            high = sorted(new_data)
            y_axis = 0
            for i in data.list_score:
                if high[-1] == int(i['score']):
                    stage.text(f"High score {i['name']} : {i['score']}", 30, -80 + y_axis)
                    y_axis -= 35

            Screen().exitonclick()

        if stage.data.score == num_pipe:
            stage.text(" ALL CLEAR!! ", 50, -5)
            Screen().exitonclick()

