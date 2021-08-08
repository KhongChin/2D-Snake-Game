from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create a snake"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Keep moving the snake forward by the given distance"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Snake's head will face upwards"""
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)

    def down(self):
        """Snake's head will face downwards"""
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)

    def left(self):
        """Snake's head will turn left"""
        if self.head.heading() != EAST:
            self.head.setheading(WEST)

    def right(self):
        """Snake's head will turn right"""
        if self.head.heading() != WEST:
            self.head.setheading(EAST)





