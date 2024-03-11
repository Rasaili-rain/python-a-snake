from turtle import Screen, Turtle

MOVE_DISTANCE = 20
STARTIN_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 0
RIGHT = 180


class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()

    def create_snake(self) -> None:
        for position in STARTIN_POSITIONS:
            self.add_segment(position)
        self.head = self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment_no in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_no-1].xcor()
            new_y = self.segments[segment_no-1].ycor()
            self.segments[segment_no].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def right(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def kill_snake(self):
        for snake_body in self.segments:
            snake_body.reset()
        self.segments.clear()
