from turtle import Turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
up=90
down=270
left=180
right=0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()


    def create_snake(self):
       for i in starting_positions:
            self.add_segments(i)

    def add_segments(self,position):
        new_position = Turtle("square")
        new_position.color("white")
        new_position.penup()
        new_position.goto(position)
        self.segments.append(new_position)

    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading() != down:
            self.segments[0].setheading(up)

    def down(self):
        if self.segments[0].heading() != up:
            self.segments[0].setheading(down)

    def left(self):
        if self.segments[0].heading() != right:
            self.segments[0].setheading(left)

    def right(self):
        if self.segments[0].heading() != left:
            self.segments[0].setheading(right)

    def reset(self):
        for i in self.segments:
            i.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.segments[0]