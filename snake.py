DISTANCE = 20

from turtle import Turtle

class Snake:
    def __init__(self):
        self.t = Turtle()
        self.length = 3
        self.create_snake()
        
        
    def create_snake(self):
        self.t.shape("square")
        self.t.color("white")
        self.t.resizemode("user")
        self.t.turtlesize(stretch_len=self.length)
        self.t.penup()
        
    def move(self):
        self.t.forward(DISTANCE)
        
        
    def speed(self):
        self.t.speed('fastest')
        
    def up(self):
        
            self.t.setheading(90)

    def down(self):
        
            self.t.setheading(270)

    def left(self):
        
            self.t.setheading(180)

    def right(self):
        
            self.t.setheading(0)
            
    def distance(self,obj):
            return self.t.distance(obj)

    def grow(self):
        self.length+=1
        self.t.turtlesize(stretch_len=self.length)
        
    def collide(self):
        xcoord = self.t.xcor()
        ycoord = self.t.ycor()
        
        if xcoord>=280 or xcoord<=-280 or ycoord>=280 or ycoord<=-280:
            return True
        
        return False