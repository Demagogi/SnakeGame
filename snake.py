from turtle import Turtle  # import Turtle class from turtle module
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        """creates snake( 3 segment long) from the starting positions"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """add segment at the end of the segments(snake)"""
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        """add new segment to the snake!"""
        self.add_segment(self.segments[-1].position())

    def reset(self):  # added after update
        """resets the snake position after collision with wall or tail"""
        for seg in self.segments:
            seg.goto(5000, 5000)  # sending away snake fragments from the visible screen witch is 600x600
        self.segments.clear()
        self.create_snake()
        self.snake_head = self.segments[0]

    def move(self):
        """ first segment starts moving forward and the rest of segments move to front segment position"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_num - 1].xcor()
            y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x, y)
        self.snake_head.forward(MOVE_DISTANCE)

    def left(self):
        """ moves snake head to left"""
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        """ moves snake head to right"""
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def up(self):
        """ moves snake head to up"""
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        """ moves snake head to down"""
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)
