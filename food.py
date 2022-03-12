from turtle import Turtle  # import Turtle class from turtle module
import random  # import random module


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("cyan")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """ generates turtle(food) at the random spot on the screen"""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
