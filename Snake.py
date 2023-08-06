import turtle
starting_positions = [(0,0),(-20,0),(-40,0)]
E = 0
N = 90
W = 180
S = 270     
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self) :    
        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        snake_segment = turtle.Turtle("square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.segments.append(snake_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
         
    def move(self):
        for segment_number in range(len(self.segments)-1, 0 , -1):      
            next_x = self.segments[segment_number -1].xcor()
            next_y = self.segments[segment_number-1].ycor()
            self.segments[segment_number].goto(next_x, next_y)

        self.head.forward(20)


    def down(self):
        if (self.head.heading() != 90):
            self.head.setheading(270)
            
    def right(self):
        if (self.head.heading() != 180):
            self.head.setheading(0)
        
    def left(self):
        if (self.head.heading() != 0):
            self.head.setheading(180)

    def up(self):
        if (self.head.heading() != 270):
            self.head.setheading(90)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
            
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

            
