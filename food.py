from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.shape("circle")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.move_to_random()
        
    def move_to_random(self):
        random_x=randint(-280,280)
        random_y=randint(-280,280)
        self.setposition(random_x,random_y)